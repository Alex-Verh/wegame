from fastapi import APIRouter, Request, Response
from fastapi_sso.sso.google import GoogleSSO

from ...dependencies import DatabaseDep
from ...settings import settings
from ...users.crud import create_user, get_user_by_email
from ...users.schemas import UserCreate
from .. import crud
from ..dependencies import ClientInfoDep
from ..schemas import AuthSession, Token
from ..utils import create_tokens

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
    tokens = create_tokens(db_user.id)

    auth_session = crud.get_auth_session(
        db, user_id=db_user.id, **client_info.model_dump()
    )
    if auth_session:
        crud.update_auth_session(db, auth_session, tokens["refresh"])
    else:
        crud.create_auth_session(
            db,
            AuthSession(
                user_id=db_user.id,
                refresh_token=tokens["refresh"],
                **client_info.model_dump()
            ),
        )

    response.set_cookie(
        key="refresh_token",
        value=tokens["refresh"],
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
        httponly=True,
    )
    return Token(access_token=tokens["access"], token_type="bearer")
