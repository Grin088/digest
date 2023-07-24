import hashlib

from api.db import User
from api.db.session import SessionLocal
from api.schemas import UserCreate as UserSchema
from api.services.exceptions.utils import check_object


class UserService:
    """Class service to handle user model"""

    def user_register(self, user: UserSchema):
        """Method to create user in db"""
        with SessionLocal() as session:
            hashed_password = hashlib.sha256(
                user.password.encode(), usedforsecurity=True
            ).hexdigest()
            check_object(
                obj=User, session=session, obj_not_exist=True, username=user.username, email=user.email
            )
            user_obj = User(
                username=user.username,
                email=user.email,
                password_hash=hashed_password,
            )
            session.add(user_obj)
            session.commit()
            session.refresh(user_obj)

    def get_all_users(self):
        """Method to get all users from db"""
        with SessionLocal() as session:
            users = session.query(User).all()
        return users
