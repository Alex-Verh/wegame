from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.get("/")
async def read_languages():
    pass


@router.get("/{language_id}")
async def read_language(language_id: str):
    pass


@router.post("/")
async def create_language(language: None):
    pass


@router.delete("/{language_id}")
async def delete_language(language_id: str):
    pass
