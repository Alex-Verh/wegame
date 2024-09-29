from fastapi import HTTPException
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str
    status_code: int
