from typing import Annotated

from app.schemas.auth import ClientInfo
from app.services.auth import AuthService, get_client_info, get_current_user_id
from fastapi import Depends

CurrentUserIdDep = Annotated[int, Depends(get_current_user_id)]
ClientInfoDep = Annotated[ClientInfo, Depends(get_client_info)]

from app.models.users import User as UserModel
from app.schemas.users import User
from app.services.users import UsersService, get_current_superuser, get_current_user

CurrentUserDep = Annotated[User, Depends(get_current_user)]

SuperuserDep = Annotated[User, Depends(get_current_superuser)]

AuthService.user_model = UserModel
AuthServiceDep = Annotated[AuthService, Depends()]

UsersServiceDep = Annotated[UsersService, Depends()]
