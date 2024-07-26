from fastapi import APIRouter, Depends, HTTPException, status

from .. import crud
from ..dependencies import DatabaseDep, get_current_superuser
from ..schemas import (
    Game,
    GameCreate,
    Language,
    LanguageCreate,
    Platform,
    PlatformCreate,
)

router = APIRouter(tags=["Common"])


@router.get("/games")
def read_games(db: DatabaseDep) -> list[Game]:
    return crud.get_games(db)


@router.get("/games/{game_id}")
def read_game(db: DatabaseDep, game_id: int) -> Game:
    game = crud.get_game(db, game_id)
    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Game not found"
        )
    return game


@router.post("/games", dependencies=[Depends(get_current_superuser)])
def create_game(db: DatabaseDep, game: GameCreate) -> Game:
    return crud.create_game(db, game)


@router.delete("/games/{game_id}", dependencies=[Depends(get_current_superuser)])
def delete_game(db: DatabaseDep, game_id: int):
    return {"deleted items": crud.delete_game(db, game_id)}


@router.get("/languages")
def read_languages(db: DatabaseDep) -> list[Language]:
    return crud.get_languages(db)


@router.get("/languages/{language_id}")
def read_language(db: DatabaseDep, language_id: int) -> Language:
    language = crud.get_language(db, language_id)
    if not language:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Language not found"
        )
    return language


@router.post("/languages", dependencies=[Depends(get_current_superuser)])
def create_language(db: DatabaseDep, language: LanguageCreate) -> Language:
    return crud.create_language(db, language)


@router.delete(
    "/languages/{language_id}", dependencies=[Depends(get_current_superuser)]
)
async def delete_language(db: DatabaseDep, language_id: int):
    return {"deleted items": crud.delete_language(db, language_id)}


@router.get("/platforms")
def read_platforms(db: DatabaseDep) -> list[Platform]:
    return crud.get_platforms(db)


@router.get("/platforms/{platform_id}")
def read_platform(db: DatabaseDep, platform_id: int) -> Platform:
    platform = crud.get_platform(db, platform_id)
    if not platform:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Platform not found"
        )
    return platform


@router.post("/platforms", dependencies=[Depends(get_current_superuser)])
async def create_platform(db: DatabaseDep, platform: PlatformCreate) -> Platform:
    return crud.create_platform(db, platform)


@router.delete(
    "/platforms/{platform_id}", dependencies=[Depends(get_current_superuser)]
)
async def delete_platform(db: DatabaseDep, platform_id: int):
    return {"deleted items": crud.delete_platform(db, platform_id)}
