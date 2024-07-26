from fastapi import APIRouter, FastAPI

from .routers import applications, auth, common, parties, users

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
