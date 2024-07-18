from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


fake_applications = {
    "app1": {"title": "Application for CSGO"},
    "app2": {"title": "I find a friend for Rust"},
}


@router.get("/")
async def read_applications():
    return fake_applications


@router.get("/{application_id}")
async def read_application(application_id: str):
    if application_id not in fake_applications:
        raise HTTPException(status_code=404, detail="Application not found")
    return {
        "title": fake_applications[application_id]["title"],
        "application_id": application_id,
    }


@router.put(
    "/{application_id}",
)
async def update_application(application_id: str):
    if application_id != "app1":
        raise HTTPException(
            status_code=403, detail="You can only update the application: app1"
        )
    return {"application_id": application_id, "title": "Updated application"}
