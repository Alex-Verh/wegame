from app.database import get_db
from app.dependencies import get_current_superuser
from app.models import games as models
from app.schemas import games as schemas
from fastapi import Depends
from lib.crud_router import CRUDRouter

router = CRUDRouter(
    schema=schemas.Game,
    create_schema=schemas.GameCreate,
    db_model=models.Game,
    db=get_db,
    prefix="games",
    tags=["Games"],
    create_route=[Depends(get_current_superuser)],
    update_route=[Depends(get_current_superuser)],
    delete_one_route=[Depends(get_current_superuser)],
    delete_all_route=[Depends(get_current_superuser)],
)
