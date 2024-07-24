from fastapi import APIRouter

router = APIRouter(
    prefix="/platforms",
    tags=["Platforms"],
)


@router.get("/")
async def read_platforms():
    pass


@router.get("/{platform_id}")
async def read_platform(platform_id: str):
    pass


@router.post("/")
async def create_platform(platform: None):
    pass


@router.delete("/{platform_id}")
async def delete_platform(platform_id: str):
    pass
