from fastapi import APIRouter

from api import schemas
from api.services.users.users_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def read_root():
    return {"message": "Hello World"}


@router.get("/users")
def get_users() -> list:
    """
    Test
    :return: users
    """
    user_service = UserService()
    users = user_service.get_all_users()
    return users


@router.put("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    """
    Test
    :return: users
    """
    user_service = UserService()
    user_service.user_register(user)
    return user
