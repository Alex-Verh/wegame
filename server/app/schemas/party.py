from pydantic import BaseModel

from .common import Game, Platform
from .user import User


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
