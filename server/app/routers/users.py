from fastapi import APIRouter, HTTPException

from .. import crud
from ..dependencies import CurrentUserDep, DatabaseDep
from ..schemas import User, UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def read_users():
    pass


@router.get("/me")
def read_user_me(current_user: CurrentUserDep) -> User:
    return current_user


@router.get("/{username}")
async def read_user(username: str):
    pass


@router.post("/")
async def create_user(db: DatabaseDep, user_data: UserCreate) -> User:
    user = crud.get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists.",
        )

    user = crud.create_user(db, user_data)
    return user


@router.patch("/{username}")
async def update_user(username: str, user: None):
    pass


@router.delete("/{username}")
async def delete_user(username: str):
    pass


@router.get("/{username}/languages")
async def read_user_languages():
    pass


@router.post("/{username}/languages")
async def create_user_language(user_language: None):
    pass


@router.delete("/{username}/languages/{language_id}")
async def delete_user_language(language_id: str):
    pass


@router.get("/{username}/platforms")
async def read_user_platforms():
    pass


@router.post("/{username}/platforms")
async def create_user_platform(user_platform: None):
    pass


@router.delete("/{username}/platforms/{platform_id}")
async def delete_user_platform(platform_id: str):
    pass


@router.get("/{username}/parties")
async def read_user_parties(username: str):
    pass
