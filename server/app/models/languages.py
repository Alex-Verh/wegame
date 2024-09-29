from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
