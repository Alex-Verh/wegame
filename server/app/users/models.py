from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    age = Column(Integer)
    profile_pic = Column(String)

    is_active = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    applications = relationship("Application", back_populates="author")
    own_parties = relationship("Party", back_populates="leader")
    member_parties = relationship("PartyMember", back_populates="user")
    languages = relationship("UserLanguage", back_populates="user")
    platforms = relationship("UserPlatform", back_populates="user")


class UserLanguage(Base):
    __tablename__ = "user_languages"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    language_id = Column(Integer, ForeignKey("languages.id"), primary_key=True)

    user = relationship("User", back_populates="languages")
    language = relationship("Language")


class UserPlatform(Base):
    __tablename__ = "user_platforms"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    platform_id = Column(Integer, ForeignKey("platforms.id"), primary_key=True)

    user = relationship("User", back_populates="platforms")
    platform = relationship("Platform")
