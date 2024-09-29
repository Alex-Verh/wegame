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
