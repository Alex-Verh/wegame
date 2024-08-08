from fastapi import APIRouter, Request, Response
from fastapi_sso.sso.google import GoogleSSO

from ...dependencies import DatabaseDep
from ...settings import settings
from ...users.crud import create_user, get_user_by_email
from ...users.schemas import UserCreate
from ..dependencies import ClientInfoDep
from ..utils import authorize_user

google_sso = GoogleSSO(
    settings.GOOGLE_CLIENT_ID,
    settings.GOOGLE_CLIENT_SECRET,
    settings.GOOGLE_CALLBACK_URL,
)


router = APIRouter(
    prefix="/google",
)


@router.get("/login")
async def google_login():
    with google_sso:
        return await google_sso.get_login_redirect(
            params={"prompt": "consent", "access_type": "offline"}
        )


@router.get("/callback")
async def google_callback(
    db: DatabaseDep, client_info: ClientInfoDep, request: Request, response: Response
):
    with google_sso:
        user = await google_sso.verify_and_process(request)
        db_user = get_user_by_email(db, user.email)
    if not db_user:
        db_user = create_user(
            db,
            UserCreate(
                nickname=user.display_name,
                email=user.email,
                profile_pic=user.picture,
                age=0,
                password="",
            ),
        )
    return authorize_user(db, db_user.id, client_info, response)
