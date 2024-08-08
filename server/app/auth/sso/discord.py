from typing import Any, Dict

from fastapi import APIRouter, Request, Response
from fastapi_sso.sso.base import DiscoveryDocument, OpenID
from fastapi_sso.sso.generic import create_provider

from ...dependencies import DatabaseDep
from ...settings import settings
from ...users.crud import create_user, get_user_by_email
from ...users.schemas import UserCreate
from ..dependencies import ClientInfoDep
from ..utils import authorize_user


def convert_openid(response: Dict[str, Any], _client) -> OpenID:
    print(response)
    return OpenID(
        id=response.get("id"),
        email=response.get("email"),
        display_name=response.get("username"),
        picture=response.get("avatar"),
    )


discovery_document: DiscoveryDocument = {
    "authorization_endpoint": "https://discord.com/oauth2/authorize",
    "token_endpoint": "https://discord.com/api/oauth2/token",
    "userinfo_endpoint": "https://discord.com/api/users/@me",
}

DiscordSSO = create_provider(
    name="discord",
    default_scope=["identify", "email"],
    discovery_document=discovery_document,
    response_convertor=convert_openid,
)

discord_sso = DiscordSSO(
    client_id=settings.DISCORD_CLIENT_ID,
    client_secret=settings.DISCORD_CLIENT_SECRET,
    redirect_uri=settings.DISCORD_CALLBACK_URL,
    allow_insecure_http=True,
)


router = APIRouter(
    prefix="/discord",
)


@router.get("/login")
async def discord_login():
    """Generate login url and redirect"""
    with discord_sso:
        return await discord_sso.get_login_redirect()


@router.get("/callback")
async def discord_callback(
    db: DatabaseDep, client_info: ClientInfoDep, request: Request, response: Response
):
    with discord_sso:
        user = await discord_sso.verify_and_process(request)
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
