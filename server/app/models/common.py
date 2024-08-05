from sqlalchemy import Column, Integer, String

from ..database import Base


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    photo = Column(String)
    icon = Column(String)
    ranking = Column(String)


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)


class Platform(Base):
    __tablename__ = "platforms"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
