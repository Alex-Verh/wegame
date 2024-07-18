from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

fake_users = [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/")
async def read_users():
    return fake_users

@router.post("/")
async def create_user(user:None):
    return user

@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}

@router.patch("/{username}")
async def edit_user(username: str, user:None):
    return {"username": username, "updated_fields": user.dict(exclude_unset=True)}

@router.delete("/{username}")
async def delete_user(username: str):
    return 