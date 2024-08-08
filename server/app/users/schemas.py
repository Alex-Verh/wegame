from pydantic import BaseModel

from ..common.schemas import Language, Platform


class UserBase(BaseModel):
    nickname: str
    email: str
    age: int
    profile_pic: str | None = None


class UserUpdate(UserBase):
    password: str | None


class UserCreate(UserBase):
    password: str
    language_ids: list[int] = []
    platform_ids: list[int] = []


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    languages: list[Language] = []
    platforms: list[Platform] = []

    class Config:
        from_attributes = True
