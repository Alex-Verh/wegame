from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/party_members",
    tags=["Party Members"],
)


fake_party_members = [{"party": "2", "username": "govnoed229"}, {"party": "2", "username": "debilka201"} ]


@router.get("/")
async def read_party_members():
    return fake_party_members

@router.post("/")
async def create_party_member(user_language: None):
    return user_language

@router.get("/{party_id}")
async def read_party_members(party_id: str):
    if party_id not in None: # Check in parties
        raise HTTPException(status_code=404, detail="Party not found")
    return

@router.get("/{username}")
async def read_user_parties(username: str):
    if username not in None: # Check in users
        raise HTTPException(status_code=404, detail="User not found")
    return 

@router.delete("/{party_member_id}")
async def delete_party_member(party_member_id: str):
    if party_member_id not in fake_party_members:
        raise HTTPException(status_code=404, detail="Party member not found")
    return 