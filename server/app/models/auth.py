from app.models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class AuthSession(Base):
    __tablename__ = "auth_sessions"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    refresh_token = Column(String, index=True)
    ip_address = Column(String, primary_key=True)
    user_agent = Column(String, primary_key=True)
