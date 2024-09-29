from typing import Annotated

from fastapi import Depends, HTTPException

from app.database import DatabaseDep, db_decorator
from app.dependencies import CurrentUserIdDep
from app.mixins import HashingMixin
from app.models.users import Language as LanguageModel
from app.models.users import Platform as PlatformModel
from app.models.users import User as UserModel
from app.schemas.base import MessageResponse
from app.schemas.users import Language, Platform, User, UserCreate, UserUpdate
from app.services.base import BaseDataManager, BaseService


def get_current_user(db: DatabaseDep, user_id: CurrentUserIdDep) -> UserModel:

    user = UsersDataManager(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


def get_current_superuser(
    current_user: Annotated[UserModel, Depends(get_current_user)]
) -> UserModel:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    return current_user


class UsersService(BaseService):
    def __init__(self, db_session: DatabaseDep) -> None:
        super().__init__(db_session)
        self.data_manager = UsersDataManager(db_session)

    def create_user(self, user: UserCreate) -> User:
        return self.data_manager.create_user(user)

    def read_user(self, user_id: int) -> User:
        return self.data_manager.get_user(user_id)

    def read_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        return self.data_manager.get_users(skip, limit)

    def update_user(self, user: UserModel, user_update: UserUpdate) -> User:
        return self.data_manager.update_user(user, user_update)

    def delete_user(self, user: UserModel) -> None:
        self.data_manager.delete_user(user)
        return MessageResponse(message="User deleted", status_code=200)

    def create_user_language(self, user: UserModel, language_id: int) -> None:
        return self.data_manager.create_user_language(user, language_id)

    def delete_user_language(
        self, user: UserModel, language_id: int
    ) -> MessageResponse:
        self.data_manager.delete_user_language(user, language_id)
        return MessageResponse(message="User language deleted", status_code=200)

    def create_user_platform(self, user: UserModel, platform_id: int) -> None:
        return self.data_manager.create_user_platform(user, platform_id)

    def delete_user_platform(
        self, user: UserModel, platform_id: int
    ) -> MessageResponse:
        self.data_manager.delete_user_platform(user, platform_id)
        return MessageResponse(message="User platform deleted", status_code=200)


class UsersDataManager(BaseDataManager):

    def get_user(self, user_id: int) -> UserModel | None:
        return self.get_one_by_pk(UserModel, user_id)

    def get_users(self, skip: int = 0, limit: int = 100) -> list[UserModel]:
        return self.get_all(UserModel, skip=skip, limit=limit)

    def get_user_by_email(self, email: str) -> UserModel | None:
        return self.get_one_by_kwargs(UserModel, email=email)

    def create_user(self, user: UserCreate) -> UserModel:
        db_user = UserModel(**user.model_dump(exclude=("language_ids", "platform_ids")))
        db_user.password = HashingMixin.hash(user.password)
        for language_id in user.language_ids:
            db_user.languages.append(self.get_one_by_pk(LanguageModel, language_id))
        for platform_id in user.platform_ids:
            db_user.platforms.append(self.get_one_by_pk(PlatformModel, platform_id))

        return self.add_one(db_user)

    def update_user(self, db_user: UserModel, user_update: UserUpdate) -> UserModel:
        user_data = user_update.model_dump(exclude_unset=True)
        if "password" in user_data:
            user_data["password"] = HashingMixin.hash(user_data["password"])

        return self.update_one(db_user, **user_data)

    def delete_user(self, user: UserModel) -> None:
        self.delete_one(user)

    def create_user_language(self, user: UserModel, language_id: int) -> list[Language]:
        user.languages.append(self.get_one_by_pk(LanguageModel, language_id))
        self.db.commit()
        return user.languages

    def delete_user_language(self, user: UserModel, language_id: int) -> None:
        user.languages.remove(self.get_one_by_pk(LanguageModel, language_id))
        self.db.commit()

    def create_user_platform(self, user: UserModel, platform_id: int) -> list[Platform]:
        user.platforms.append(self.get_one_by_pk(PlatformModel, platform_id))
        self.db.commit()
        return user.platforms

    def delete_user_platform(self, user: UserModel, platform_id: int) -> None:
        user.platforms.remove(self.get_one_by_pk(PlatformModel, platform_id))
        self.db.commit()
