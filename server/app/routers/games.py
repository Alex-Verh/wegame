from fastapi import APIRouter

router = APIRouter(
    prefix="/games",
    tags=["Games"],
)


@router.get("/")
async def read_games():
    pass


@router.get("/{game_id}")
async def read_game(game_id: str):
    pass


@router.post("/")
async def create_game(game: None):
    pass


@router.delete("/{game_id}")
async def delete_game(game_id: str):
    pass
