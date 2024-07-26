from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int


class AuthSession(BaseModel):
    user_id: int
    ip_address: str
    user_agent: str
    refresh_token: str = ""

    class Config:
        from_attributes = True


class ClientInfo(BaseModel):
    ip_address: str
    user_agent: str
