from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# TODO add relationships
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    profile_pic = Column(String)

    applications = relationship("Application", back_populates="author")
    own_parties = relationship("Party", back_populates="leader")
    languages = relationship("UserLanguage", back_populates="user")
    platforms = relationship("UserPlatform", back_populates="user")


class Application(Base):
    __tablename__ = "applications"
    id = Column(Integer, primary_key=True)
    author_id = Column(String, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    title = Column(String, index=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"))
    ranking = Column(String)

    author = relationship("User", back_populates="applications")


class Party(Base):
    id = Column(Integer, primary_key=True)
    leader_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    age_range = Column(String)
    platform_id = Column(Integer, ForeignKey("platforms.id"))

    leader = relationship("User", back_populates="own_parties")


class PartyMember(Base):
    __tablename__ = "party_members"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    party_id = Column(Integer, ForeignKey("parties.id"), primary_key=True)


class Language(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)


class UserLanguage(Base):
    __tablename__ = "user_languages"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    language_id = Column(Integer, ForeignKey("languages.id"), primary_key=True)

    user = relationship("User", back_populates="languages")


class Platform(Base):
    __tablename__ = "platforms"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)


class UserPlatform(Base):
    __tablename__ = "user_platforms"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"), primary_key=True)

    user = relationship("User", back_populates="platforms")


class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    photo = Column(String)
    icon = Column(String)
    ranking = Column(String)
