from typing import Annotated

from app.dependencies import AuthServiceDep, ClientInfoDep, CurrentUserIdDep
from app.schemas.auth import Token
from app.schemas.base import MessageResponse
from app.sso.discord import discord_sso
from app.sso.google import google_sso
from fastapi import APIRouter, Cookie, Depends, Request, Response
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/login")
def login(
    auth_service: AuthServiceDep,
    client_info: ClientInfoDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    response: Response,
) -> Token:
    return auth_service.login(
        form_data.username, form_data.password, client_info, response
    )


@router.get("/logout")
def logout(
    auth_service: AuthServiceDep,
    current_user_id: CurrentUserIdDep,
    client_info: ClientInfoDep,
    response: Response,
) -> MessageResponse:

    return auth_service.logout(current_user_id, client_info, response)


@router.get("/refresh")
def refresh(
    auth_service: AuthServiceDep,
    refresh_token: Annotated[str, Cookie()],
    response: Response,
) -> Token:
    return auth_service.refresh(refresh_token, response)


discord_router = APIRouter(prefix="/discord", tags=["Auth"])


@discord_router.get("/login")
async def discord_login(auth_service: AuthServiceDep):
    return await auth_service.sso_login(discord_sso)


@discord_router.get("/callback")
async def discord_callback(
    auth_service: AuthServiceDep,
    client_info: ClientInfoDep,
    request: Request,
    response: Response,
):
    return await auth_service.sso_callback(discord_sso, client_info, request, response)


router.include_router(discord_router)

google_router = APIRouter(prefix="/google", tags=["Auth"])


@google_router.get("/login")
async def google_login(auth_service: AuthServiceDep):
    return await auth_service.sso_login(google_sso)


@google_router.get("/callback")
async def google_callback(
    auth_service: AuthServiceDep,
    client_info: ClientInfoDep,
    request: Request,
    response: Response,
):
    return await auth_service.sso_callback(google_sso, client_info, request, response)


router.include_router(google_router)
