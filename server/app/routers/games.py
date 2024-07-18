from fastapi import APIRouter

router = APIRouter(
    prefix="/games",
    tags=["Games"],
)


fake_games = ["CSGO", "Rust", "SCUM", "DayZ"]


@router.get("/")
async def read_games():
    return fake_games
