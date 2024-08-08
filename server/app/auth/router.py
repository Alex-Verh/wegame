from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from ..dependencies import DatabaseDep
from ..settings import settings
from . import crud
from .dependencies import ClientInfoDep, CurrentUserIdDep
from .schemas import Token, TokenPayload
from .security import read_token
from .sso import discord, google
from .utils import authenticate_user, authorize_user, create_tokens

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)
router.include_router(google.router)
router.include_router(discord.router)


@router.post("/login")
def login(
    db: DatabaseDep,
    client_info: ClientInfoDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    response: Response,
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return authorize_user(db, user.id, client_info, response)


@router.get("/logout")
def logout(
    db: DatabaseDep,
    current_user_id: CurrentUserIdDep,
    client_info: ClientInfoDep,
    response: Response,
) -> dict[str, str]:

    if not crud.delete_auth_session(
        db, user_id=current_user_id, **client_info.model_dump()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid IP address or user agent",
        )
    response.delete_cookie("refresh_token")

    return {"message": "Successfully logged out"}


@router.get("/refresh")
def refresh(
    db: DatabaseDep, refresh_token: Annotated[str, Cookie()], response: Response
) -> Token:
    try:
        token_data = TokenPayload(**read_token(refresh_token))
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    db_token = crud.get_auth_session_by_refresh_token(db, refresh_token)
    if not db_token or db_token.user_id != token_data.sub:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )

    tokens = create_tokens(token_data.sub)

    crud.update_auth_session(db, db_token, tokens["refresh"])

    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh"],
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
        httponly=True,
    )
    return Token(access_token=tokens["access"], token_type="bearer")
