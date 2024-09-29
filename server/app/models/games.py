from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    photo = Column(String)
    icon = Column(String)
    ranking = Column(String)
