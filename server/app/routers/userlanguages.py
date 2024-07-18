from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/user_language",
    tags=["User Languages"],
)


fake_user_languages = [{"username": "rickroll22", "language": "Russian"}, {"username": "rickroll22", "language": "English"} ]


@router.get("/")
async def read_user_languages():
    return fake_user_languages

@router.post("/")
async def create_user_language(user_language: None):
    return user_language

@router.get("/{username}")
async def read_user_languages(username: str):
    if username not in None: # Check in users
        raise HTTPException(status_code=404, detail="User not found")
    return 

@router.delete("/{user_language_id}")
async def delete_user_language(user_language_id: str):
    if user_language_id not in fake_user_languages:
        raise HTTPException(status_code=404, detail="User language not found")
    return 