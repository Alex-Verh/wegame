from fastapi import APIRouter, FastAPI

from .applications import router as applications
from .auth import router as auth
from .common import router as common
from .parties import router as parties
from .users import router as users

app = FastAPI()

app_router = APIRouter(prefix="/api")
app_router.include_router(auth.router)
app_router.include_router(users.router)
app_router.include_router(applications.router)
app_router.include_router(parties.router)
app_router.include_router(common.router)
app.include_router(app_router)


@app.get("/")
async def root():
    return {"message": "Wegame"}
