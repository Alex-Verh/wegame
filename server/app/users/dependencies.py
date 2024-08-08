from typing import Annotated

from fastapi import Depends, HTTPException

from ..auth.dependencies import CurrentUserIdDep
from ..dependencies import DatabaseDep
from . import crud
from .models import User as DbUser
from .schemas import User


def get_current_user(db: DatabaseDep, user_id: CurrentUserIdDep) -> DbUser:

    user = crud.get_user(db, user_id)
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
