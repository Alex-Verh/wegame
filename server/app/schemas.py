from pydantic import BaseModel


class Language(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class Platform(BaseModel):
    id: int
    title: str
    url: str

    class Config:
        from_attributes = True


class Game(BaseModel):
    id: int
    title: str
    photo: str
    icon: str
    ranking: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    nickname: str
    email: str
    age: int
    profile_pic: str | None = None


class UserCreate(UserBase):
    password: str
    language_ids: list[int] = []
    platform_ids: list[int] = []


class User(UserBase):
    id: int
    languages: list[Language] = []
    platforms: list[Platform] = []

    class Config:
        from_attributes = True


class ApplicationBase(BaseModel):
    title: str
    ranking: str | None = None


class ApplicationCreate(ApplicationBase):
    author_id: int
    game_id: int
    platform_id: int


class Application(ApplicationBase):
    id: int
    author: User
    game: Game
    platform: Platform

    class Config:
        from_attributes = True


class PartyBase(BaseModel):
    age_range: str


class PartyCreate(PartyBase):
    leader_id: int
    game_id: int
    platform_id: int


class Party(PartyBase):
    id: int
    leader: User
    members: list[User] = []
    game: Game
    platform: Platform

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None


class UserInDB(UserBase):
    id: int
    hashed_password: str
