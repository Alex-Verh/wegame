from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

fake_users = [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/")
async def read_users():
    return fake_users


@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}
