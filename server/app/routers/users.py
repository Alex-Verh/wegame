from fastapi import APIRouter, Depends, HTTPException

from .. import crud
from ..dependencies import CurrentUserDep, DatabaseDep, get_current_superuser
from ..schemas import DeletionResponse, User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def read_user_me(current_user: CurrentUserDep) -> User:
    return current_user


@router.patch("/me")
def update_user_me(
    db: DatabaseDep, current_user: CurrentUserDep, user: UserUpdate
) -> User:
    return crud.update_user(db, current_user, user)


@router.delete("/me")
def delete_user_me(db: DatabaseDep, current_user: CurrentUserDep) -> DeletionResponse:
    return DeletionResponse(deleted_items=crud.delete_user(db, current_user))


@router.get("/{user_id}")
def read_user(db: DatabaseDep, user_id: int) -> User:
    return crud.get_user(db, user_id)


@router.get("/", dependencies=[Depends(get_current_superuser)])
def read_users(db: DatabaseDep) -> list[User]:
    return crud.get_users(db)


@router.post("/")
def create_user(db: DatabaseDep, user_data: UserCreate) -> User:
    user = crud.get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists.",
        )

    user = crud.create_user(db, user_data)
    return user


@router.patch("/{user_id}", dependencies=[Depends(get_current_superuser)])
def update_user(db: DatabaseDep, user_id: int, user: UserUpdate) -> User:
    return crud.update_user(db, user_id, user)


@router.delete("/{user_id}", dependencies=[Depends(get_current_superuser)])
def delete_user(db: DatabaseDep, user_id: int) -> DeletionResponse:
    return DeletionResponse(deleted_items=crud.delete_user(db, user_id))


@router.get("/{username}/languages")
def read_user_languages():
    pass


@router.post("/{username}/languages")
def create_user_language(user_language: None):
    pass


@router.delete("/{username}/languages/{language_id}")
def delete_user_language(language_id: str):
    pass


@router.get("/{username}/platforms")
def read_user_platforms():
    pass


@router.post("/{username}/platforms")
def create_user_platform(user_platform: None):
    pass


@router.delete("/{username}/platforms/{platform_id}")
def delete_user_platform(platform_id: str):
    pass


@router.get("/{username}/parties")
def read_user_parties(username: str):
    pass
