from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class User(Base):
    """
    User model
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    subscriptions = relationship(
        "Subscription", back_populates="user", cascade="all, delete-orphan"
    )
    digests = relationship(
        "Digest", back_populates="user", cascade="all, delete-orphan"
    )
