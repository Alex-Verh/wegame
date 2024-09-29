from typing import Any, Dict

from app.settings import settings
from fastapi_sso.sso.base import DiscoveryDocument, OpenID
from fastapi_sso.sso.generic import create_provider


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
