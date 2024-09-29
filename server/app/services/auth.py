from datetime import timedelta
from typing import Annotated, Type

from fastapi import Depends, Header, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordBearer
from fastapi_sso import SSOBase
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from app.database import DatabaseDep
from app.mixins import HashingMixin, TokensMixin
from app.models.auth import AuthSession as AuthSessionModel
from app.models.base import Base
from app.schemas.auth import AuthSession, ClientInfo, Token, TokenPayload
from app.schemas.base import MessageResponse
from app.services.base import BaseDataManager, BaseService
from app.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")


def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]) -> int:
    try:
        token_payload = TokenPayload(**TokensMixin.read_token(token))
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_payload.sub


def get_client_info(
    user_agent: Annotated[str, Header()], request: Request
) -> ClientInfo:
    return ClientInfo(ip_address=request.client.host, user_agent=user_agent)


class AuthService(HashingMixin, TokensMixin, BaseService):

    user_model: Type[Base]  # type: ignore

    def __init__(self, db: DatabaseDep) -> None:
        super().__init__(db)
        self.data_manager = AuthDataManager(db)

    def login(
        self, email: str, password: str, client_info: ClientInfo, response: Response
    ) -> Token:

        user = self.data_manager.get_one_by_kwargs(self.user_model, email=email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not self.verify(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return self._authorize_user(user.id, client_info, response)

    def logout(
        self, user_id: int, client_info: ClientInfo, response: Response
    ) -> MessageResponse:
        if not self.data_manager.delete_auth_session(
            user_id=user_id, **client_info.model_dump()
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid IP address or user agent",
            )
        response.delete_cookie("refresh_token")

        return MessageResponse(message="Logout successful", status_code=200)

    def refresh(self, refresh_token: str, response: Response) -> Token:
        try:
            token_data = TokenPayload(**self.read_token(refresh_token))
        except (InvalidTokenError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Could not validate credentials",
            )

        db_token = self.data_manager.get_auth_session_by_refresh_token(refresh_token)
        if not db_token or db_token.user_id != token_data.sub:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token",
            )

        tokens = self._create_tokens(token_data.sub)

        self.data_manager.update_auth_session(db_token, tokens["refresh"])

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
            httponly=True,
        )
        return Token(access_token=tokens["access"], token_type="bearer")

    async def sso_login(self, sso_instance: SSOBase):
        with sso_instance:
            return await sso_instance.get_login_redirect()

    async def sso_callback(
        self,
        sso_instance: SSOBase,
        client_info: ClientInfo,
        request: Request,
        response: Response,
    ):
        with sso_instance:
            user = await sso_instance.verify_and_process(request)
            db_user = self.data_manager.get_one_by_kwargs(
                self.user_model, email=user.email
            )
        if not db_user:
            db_user = self.user_model(
                nickname=user.display_name,
                email=user.email,
                profile_pic=user.picture,
                age=0,
                password="",
            )
            db_user.password = self.hash(user.password)
            db_user = self.data_manager.add_one(db_user)
        return self._authorize_user(db_user.id, client_info, response)

    def _authorize_user(
        self, user_id: int, client_info: ClientInfo, response: Response
    ) -> Token:
        tokens = self._create_tokens(user_id)

        auth_session = self.data_manager.get_auth_session(
            user_id=user_id, **client_info.model_dump()
        )
        if auth_session:
            self.data_manager.update_auth_session(auth_session, tokens["refresh"])
        else:
            self.data_manager.create_auth_session(
                AuthSession(
                    user_id=user_id,
                    refresh_token=tokens["refresh"],
                    **client_info.model_dump()
                ),
            )

        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
            httponly=True,
        )
        return Token(access_token=tokens["access"], token_type="bearer")

    def _create_tokens(self, user_id: int) -> dict[str, str]:
        access_token = self.create_token(
            data={"sub": user_id},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        )
        refresh_token = self.create_token(
            {"sub": user_id},
            expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
        )
        return {"access": access_token, "refresh": refresh_token}


class AuthDataManager(BaseDataManager):
    def get_auth_session(
        self, user_id: int, ip_address: str, user_agent: str
    ) -> AuthSessionModel | None:
        return self.get_one_by_kwargs(
            AuthSessionModel,
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
        )

    def get_auth_session_by_refresh_token(
        self, refresh_token: str
    ) -> AuthSessionModel | None:
        return self.get_one_by_kwargs(AuthSessionModel, refresh_token=refresh_token)

    def create_auth_session(self, auth_session: AuthSession) -> AuthSessionModel:
        db_auth_session = AuthSessionModel(**auth_session.model_dump())
        return self.add_one(db_auth_session)

    def update_auth_session(
        self, db_auth_session: AuthSessionModel, refresh_token: str
    ) -> AuthSessionModel:
        return self.update_one(db_auth_session, refresh_token=refresh_token)

    def delete_auth_session(
        self, user_id: int, ip_address: str, user_agent: str
    ) -> int:
        self.delete_one_by_kwargs(
            AuthSessionModel,
            user_id=user_id,
            ip_address=ip_address,
            user_agent=user_agent,
        )
