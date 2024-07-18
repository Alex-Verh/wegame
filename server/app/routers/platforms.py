from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/platforms",
    tags=["Platforms"],
)


fake_platforms = ["XBOX", "Steam", "Epic Games", "Origin"]


@router.get("/")
async def read_platforms():
    return fake_platforms

@router.post("/")
async def create_platform(platform: None):
    return platform

@router.get("/{platform_id}")
async def read_platform(platform_id: str):
    if platform_id not in fake_platforms:
        raise HTTPException(status_code=404, detail="Platform not found")
    return {
        "title": fake_platforms[platform_id]["title"],
        "platform_id": platform_id,
    }

@router.delete("/{platform_id}")
async def delete_game(platform_id: str):
    if platform_id not in fake_platforms:
        raise HTTPException(status_code=404, detail="Platform not found")
    return 