from pydantic import BaseModel


class LanguageCreate(BaseModel):
    title: str


class Language(LanguageCreate):
    id: int

    class Config:
        from_attributes = True
