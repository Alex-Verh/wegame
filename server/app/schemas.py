from pydantic import BaseModel


class DeletionResponse(BaseModel):
    deleted_items: int
