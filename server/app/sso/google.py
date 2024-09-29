from app.settings import settings
from fastapi_sso.sso.google import GoogleSSO

google_sso = GoogleSSO(
    settings.GOOGLE_CLIENT_ID,
    settings.GOOGLE_CLIENT_SECRET,
    settings.GOOGLE_CALLBACK_URL,
)
