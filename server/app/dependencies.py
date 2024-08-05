from typing import Annotated, Generator

from fastapi import Depends, Header, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal
from .schemas import ClientInfo, TokenPayload, User
from .security import read_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")

TokenDep = Annotated[str, Depends(oauth2_scheme)]


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DatabaseDep = Annotated[Session, Depends(get_db)]


async def get_current_user(db: DatabaseDep, token: TokenDep):

    try:
        token_payload = TokenPayload(**read_token(token))
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_user(db, token_payload.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]


def get_current_superuser(current_user: CurrentUserDep) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user


SuperuserDep = Annotated[User, Depends(get_current_superuser)]


def get_client_info(
    user_agent: Annotated[str, Header()], request: Request
) -> ClientInfo:
    return ClientInfo(ip_address=request.client.host, user_agent=user_agent)


ClientInfoDep = Annotated[ClientInfo, Depends(get_client_info)]
