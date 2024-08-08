from fastapi import APIRouter

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


@router.get("/")
async def read_applications():
    pass


@router.get("/{application_id}")
async def read_application(application_id: str):
    pass


@router.post("/")
async def create_application(application: None):
    pass


@router.patch("/{application_id}")
async def update_application(application_id: str, application: None):
    pass


@router.delete("/{application_id}")
async def delete_application(application_id: str):
    pass
