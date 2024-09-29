from app.database import get_db
from app.dependencies import get_current_superuser
from app.models import languages as models
from app.schemas import languages as schemas
from fastapi import Depends
from lib.crud_router import CRUDRouter

router = CRUDRouter(
    schema=schemas.Language,
    create_schema=schemas.LanguageCreate,
    db_model=models.Language,
    db=get_db,
    prefix="languages",
    tags=["Languages"],
    create_route=[Depends(get_current_superuser)],
    update_route=[Depends(get_current_superuser)],
    delete_one_route=[Depends(get_current_superuser)],
    delete_all_route=[Depends(get_current_superuser)],
)
