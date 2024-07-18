from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/parties",
    tags=["Parties"],
)


fake_parties = {
    "party1": {"title": "First party"},
    "party2": {"title": "Second party"},
}


@router.get("/")
async def read_parties():
    return fake_parties


@router.get("/{party_id}")
async def read_party(party_id: str):
    if party_id not in fake_parties:
        raise HTTPException(status_code=404, detail="Party not found")
    return {
        "title": fake_parties[party_id]["title"],
        "party_id": party_id,
    }
