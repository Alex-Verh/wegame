from pydantic import BaseModel


class GameCreate(BaseModel):
    title: str
    photo: str
    icon: str
    ranking: str


class Game(GameCreate):
    id: int

    class Config:
        from_attributes = True


class LanguageCreate(BaseModel):
    title: str


class Language(LanguageCreate):
    id: int

    class Config:
        from_attributes = True


class PlatformCreate(BaseModel):
    title: str
    url: str


class Platform(PlatformCreate):
    id: int

    class Config:
        from_attributes = True


class DeletionResponse(BaseModel):
    deleted_items: int
