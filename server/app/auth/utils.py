from datetime import timedelta

from sqlalchemy.orm import Session

from ..security import create_token, verify_password
from ..settings import settings
from ..users.crud import get_user_by_email


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
