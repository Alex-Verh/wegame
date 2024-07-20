from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/party_members",
    tags=["Party Members"],
)


@router.get("/")
async def read_party_members():
    pass


@router.get("/{party_id}")
async def read_party_members(party_id: str):
    pass


@router.get("/{username}")
async def read_user_parties(username: str):
    pass


@router.post("/")
async def create_party_member(user_language: None):
    pass


@router.delete("/{party_member_id}")
async def delete_party_member(party_member_id: str):
    pass
