from fastapi import APIRouter

router = APIRouter(
    prefix="/parties",
    tags=["Parties"],
)


@router.get("/")
async def read_parties():
    pass


@router.get("/{party_id}")
async def read_party(party_id: str):
    pass


@router.post("/")
async def create_party(party: None):
    pass


@router.patch("/{party_id}")
async def update_party(party_id: str, party: None):
    pass


@router.delete("/{party_id}")
async def delete_party(party_id: str):
    pass


@router.get("/{party_id}/members")
async def read_party_members(party_id: str):
    pass


@router.post("/{party_id}/members")
async def create_party_member(user_language: None):
    pass


@router.delete("/{party_id}/members/{party_member_id}")
async def delete_party_member(party_member_id: str):
    pass
