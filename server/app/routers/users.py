from fastapi import APIRouter

from app.dependencies import CurrentUserDep, UsersServiceDep
from app.schemas.base import MessageResponse
from app.schemas.users import Language, Platform, User, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user_service: UsersServiceDep, user_data: UserCreate) -> User:
    return user_service.create_user(user_data)


@router.get("/")
def read_users(
    user_service: UsersServiceDep, skip: int = 0, limit: int = 20
) -> list[User]:
    return user_service.read_users(skip, limit)


@router.get("/me")
def read_user_me(current_user: CurrentUserDep) -> User:
    return current_user


@router.get("/{user_id}")
def read_user(user_service: UsersServiceDep, user_id: int) -> User:
    return user_service.read_user(user_id)


@router.patch("/me")
def update_user_me(
    user_service: UsersServiceDep,
    current_user: CurrentUserDep,
    user_update: UserUpdate,
) -> User:
    return user_service.update_user(current_user, user_update)


@router.delete("/me")
def delete_user_me(
    user_service: UsersServiceDep, current_user: CurrentUserDep
) -> MessageResponse:
    return user_service.delete_user(current_user)


user_languages = APIRouter(prefix="/me/languages", tags=["Users"])


@user_languages.post("/")
def create_user_language(
    user_service: UsersServiceDep, current_user: CurrentUserDep, language_id: int
) -> list[Language]:
    return user_service.create_user_language(current_user, language_id)


@user_languages.delete("/")
def delete_user_language(
    user_service: UsersServiceDep, current_user: CurrentUserDep, language_id: int
):
    return user_service.delete_user_language(current_user, language_id)


router.include_router(user_languages)


user_platforms = APIRouter(prefix="/me/platforms", tags=["Users"])


@user_platforms.post("/")
def create_user_platform(
    user_service: UsersServiceDep, current_user: CurrentUserDep, platform_id: int
) -> list[Platform]:
    return user_service.create_user_platform(current_user, platform_id)


@user_platforms.delete("/")
def delete_user_platform(
    user_service: UsersServiceDep, current_user: CurrentUserDep, platform_id: int
):
    return user_service.delete_user_platform(current_user, platform_id)


router.include_router(user_platforms)
