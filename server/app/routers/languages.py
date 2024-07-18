from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


fake_languages = ["Кыргыз", "Russian", "English", "Gallic"]


@router.get("/")
async def read_languages():
    return fake_languages

@router.post("/")
async def create_language(language: None):
    return language

@router.get("/{language_id}")
async def read_language(language_id: str):
    if language_id not in fake_languages:
        raise HTTPException(status_code=404, detail="Language not found")
    return {
        "title": fake_languages[language_id]["title"],
        "language_id": language_id,
    }

@router.delete("/{language_id}")
async def delete_language(language_id: str):
    if language_id not in fake_languages:
        raise HTTPException(status_code=404, detail="Language not found")
    return 