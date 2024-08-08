from typing import Annotated

from fastapi import Depends, Header, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from .schemas import ClientInfo, TokenPayload
from .security import read_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/token")

TokenDep = Annotated[str, Depends(oauth2_scheme)]


def get_current_user_id(token: TokenDep) -> int:
    try:
        token_payload = TokenPayload(**read_token(token))
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_payload.sub


CurrentUserIdDep = Annotated[int, Depends(get_current_user_id)]


def get_client_info(
    user_agent: Annotated[str, Header()], request: Request
) -> ClientInfo:
    return ClientInfo(ip_address=request.client.host, user_agent=user_agent)


ClientInfoDep = Annotated[ClientInfo, Depends(get_client_info)]
