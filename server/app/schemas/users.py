from pydantic import BaseModel

from app.schemas.languages import Language
from app.schemas.platforms import Platform


class UserBase(BaseModel):
    nickname: str
    email: str
    age: int
    profile_pic: str | None = None


class UserUpdate(BaseModel):
    password: str | None = None
    nickname: str | None = None
    email: str | None = None
    age: int | None = None
    profile_pic: str | None = None


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
