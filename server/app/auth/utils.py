from datetime import timedelta

from fastapi import Response
from sqlalchemy.orm import Session

from ..settings import settings
from ..users.crud import get_user_by_email
from . import crud
from .schemas import AuthSession, ClientInfo, Token
from .security import create_token, verify_password


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_tokens(user_id: int) -> dict[str, str]:
    access_token = create_token(
        data={"sub": user_id},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = create_token(
        {"sub": user_id},
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )
    return {"access": access_token, "refresh": refresh_token}


def authorize_user(
    db: Session, user_id: int, client_info: ClientInfo, response: Response
):
    tokens = create_tokens(user_id)

    auth_session = crud.get_auth_session(
        db, user_id=user_id, **client_info.model_dump()
    )
    if auth_session:
        crud.update_auth_session(db, auth_session, tokens["refresh"])
    else:
        crud.create_auth_session(
            db,
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
