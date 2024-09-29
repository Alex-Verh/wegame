from app.schemas.games import Game
from app.schemas.platforms import Platform
from app.schemas.users import User
from pydantic import BaseModel


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
