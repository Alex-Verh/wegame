from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/games",
    tags=["Games"],
)


fake_games = ["CSGO", "Rust", "SCUM", "DayZ"]


@router.get("/")
async def read_games():
    return fake_games

@router.post("/")
async def create_game(game: None):
    return game

@router.get("/{game_id}")
async def read_game(game_id: str):
    if game_id not in fake_games:
        raise HTTPException(status_code=404, detail="Game not found")
    return {
        "title": fake_games[game_id]["title"],
        "game_id": game_id,
    }

@router.delete("/{game_id}")
async def delete_game(game_id: str):
    if game_id not in fake_games:
        raise HTTPException(status_code=404, detail="Game not found")
    return 