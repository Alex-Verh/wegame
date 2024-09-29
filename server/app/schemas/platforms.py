from pydantic import BaseModel


class PlatformCreate(BaseModel):
    title: str
    url: str


class Platform(PlatformCreate):
    id: int

    class Config:
        from_attributes = True
