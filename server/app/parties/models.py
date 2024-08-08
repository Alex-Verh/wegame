from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Party(Base):
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True)
    leader_id = Column(Integer, ForeignKey("users.id"))
    game_id = Column(Integer, ForeignKey("games.id"))
    age_range = Column(String)
    platform_id = Column(Integer, ForeignKey("platforms.id"))

    leader = relationship("User", back_populates="own_parties")
    members = relationship("PartyMember", back_populates="party")
    platform = relationship("Platform")


class PartyMember(Base):
    __tablename__ = "party_members"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    party_id = Column(Integer, ForeignKey("parties.id"), primary_key=True)

    user = relationship("User", back_populates="member_parties")
    party = relationship("Party", back_populates="members")
