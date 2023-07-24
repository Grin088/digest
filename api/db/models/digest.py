from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class Digest(Base):
    __tablename__ = "digests"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    posts = Column(JSON)

    user = relationship(
        "User", back_populates="digests", foreign_keys=[user_id], cascade="save-update"
    )
