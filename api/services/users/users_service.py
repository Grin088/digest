import hashlib

from api.db import User
from api.db.session import SessionLocal
from api.schemas import UserCreate as UserSchema
from api.services.exceptions.utils import check_object


class UserService:
    """Class service to handle requests from user endpoints"""

    def user_register(self, user: UserSchema) -> User:
        """Method to create user in db"""
        with SessionLocal() as session:
            hashed_password = hashlib.sha256(
                user.password.encode(), usedforsecurity=True
            ).hexdigest()
            check_object(
                obj=User, session=session, obj_not_exist=True, email=user.email
            )
            check_object(
                obj=User, session=session, obj_not_exist=True, username=user.username
            )
            user_obj = User(
                username=user.username,
                email=user.email,
                hashed_password=hashed_password,
            )
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)
            return user_obj

    def get_all_users(self) -> User:
        """Method to get all users from db"""
        with SessionLocal() as session:
            users = session.query(User).all()
        return users
