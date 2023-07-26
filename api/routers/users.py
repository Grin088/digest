from fastapi import APIRouter

from api import schemas
from api.services.users.users_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
user_service = UserService()


@router.get("/")
def get_users() -> list:
    """
    API to get all users
    :return list[User]:
    """
    users = user_service.get_all_users()
    return users


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    """
    API to create user
    :param user:
    :return schemas.User:
    """
    user = user_service.user_register(user)
    return user
