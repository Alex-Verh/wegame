from fastapi import APIRouter

applications_router = APIRouter(prefix="/applications", tags=["Applications"])


@applications_router.get("", description="Get all applications")
async def get_applications():
    return ["fisrt", "second"]
