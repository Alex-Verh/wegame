from fastapi import APIRouter, FastAPI

from .applications.router import applications_router

app = FastAPI()

main_router = APIRouter()
main_router.include_router(applications_router)


app.include_router(main_router, prefix="/api")
