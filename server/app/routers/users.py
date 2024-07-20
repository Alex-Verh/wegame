from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def read_users():
    pass


@router.get("/me")
async def read_user_me():
    pass


@router.get("/{username}")
async def read_user(username: str):
    pass


@router.post("/")
async def create_user(user: None):
    pass


@router.patch("/{username}")
async def update_user(username: str, user: None):
    pass


@router.delete("/{username}")
async def delete_user(username: str):
    pass


@router.get("/{username}/languages")
async def read_user_languages():
    pass


@router.post("/{username}/languages")
async def create_user_language(user_language: None):
    pass


@router.delete("/{username}/languages/{language_id}")
async def delete_user_language(language_id: str):
    pass


@router.get("/{username}/platforms")
async def read_user_platforms():
    pass


@router.post("/{username}/platforms")
async def create_user_platform(user_platform: None):
    pass


@router.delete("/{username}/platforms/{platform_id}")
async def delete_user_platform(platform_id: str):
    pass
