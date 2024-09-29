from app.schemas.games import Game
from app.schemas.platforms import Platform
from app.schemas.users import User
from pydantic import BaseModel


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
