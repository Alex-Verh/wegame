from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from .. import crud
from ..dependencies import ClientInfoDep, CurrentUserDep, DatabaseDep
from ..schemas import AuthSession, Token, TokenPayload
from ..security import create_token, read_token, verify_password
from ..settings import settings

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_tokens(user_id: int) -> dict[str, Token]:
    access_token = create_token(
        data={"sub": user_id},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    refresh_token = create_token(
        {"sub": user_id},
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS),
    )
    return {"access": access_token, "refresh": refresh_token}


@router.post("/token")
def get_tokens(
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

    tokens = create_tokens(user.id)

    auth_session = crud.get_auth_session(
        db, user_id=user.id, **client_info.model_dump()
    )
    if auth_session:
        crud.update_auth_session(db, auth_session, tokens["refresh"])
    else:
        crud.create_auth_session(
            db,
            AuthSession(
                user_id=user.id,
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


@router.delete("/token")
def delete_tokens(
    db: DatabaseDep,
    current_user: CurrentUserDep,
    client_info: ClientInfoDep,
    response: Response,
) -> dict[str, str]:

    if not crud.delete_auth_session(
        db, user_id=current_user.id, **client_info.model_dump()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid IP address or user agent",
        )
    response.delete_cookie("refresh_token")

    return {"message": "Successfully logged out"}


@router.patch("/token")
def update_tokens(
    db: DatabaseDep, refresh_token: Annotated[str, Cookie()], response: Response
):
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
