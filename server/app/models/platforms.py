from app.models.base import Base
from sqlalchemy import Column, Integer, String


class Platform(Base):
    __tablename__ = "platforms"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False)
