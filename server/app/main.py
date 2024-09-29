from app.routers import applications, auth, games, languages, parties, platforms, users
from fastapi import APIRouter, FastAPI

app = FastAPI()

app_router = APIRouter(prefix="/api")
app_router.include_router(applications.router)
app_router.include_router(auth.router)
app_router.include_router(games.router)
app_router.include_router(languages.router)
app_router.include_router(parties.router)
app_router.include_router(platforms.router)
app_router.include_router(users.router)
app.include_router(app_router)


@app.get("/")
async def root():
    return {"message": "Wegame"}
