from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/user_platform",
    tags=["User Platforms"],
)


fake_user_platforms = [{"username": "rickroll22", "platform": "XBOX"}, {"username": "rickroll22", "platform": "PSP"} ]


@router.get("/")
async def read_user_platforms():
    return fake_user_platforms

@router.post("/")
async def create_user_platform(user_platform: None):
    return user_platform

@router.get("/{username}")
async def read_user_platforms(username: str):
    if username not in None: # Check in users
        raise HTTPException(status_code=404, detail="User not found")
    return 

@router.delete("/{user_platform_id}")
async def delete_user_platform(user_platform_id: str):
    if user_platform_id not in fake_user_platforms:
        raise HTTPException(status_code=404, detail="User platform not found")
    return 