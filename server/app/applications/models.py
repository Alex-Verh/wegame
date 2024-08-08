from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    title = Column(String, nullable=False)
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    ranking = Column(String)

    author = relationship("User", back_populates="applications")
