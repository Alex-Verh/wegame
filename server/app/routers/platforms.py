from app.database import get_db
from app.dependencies import get_current_superuser
from app.models import platforms as models
from app.schemas import platforms as schemas
from fastapi import Depends
from lib.crud_router import CRUDRouter

router = CRUDRouter(
    schema=schemas.Platform,
    create_schema=schemas.PlatformCreate,
    db_model=models.Platform,
    db=get_db,
    prefix="platforms",
    tags=["Platforms"],
    create_route=[Depends(get_current_superuser)],
    update_route=[Depends(get_current_superuser)],
    delete_one_route=[Depends(get_current_superuser)],
    delete_all_route=[Depends(get_current_superuser)],
)
