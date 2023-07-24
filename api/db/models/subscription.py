from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from api.db.base_class import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship(
        "User",
        back_populates="subscriptions",
        foreign_keys=[user_id],
        cascade="save-update",
    )
    post_categories = relationship(
        "PostCategory",
        secondary="subscription_category_association_table",
        back_populates="subscriptions",
        cascade="save-update",
    )


subscription_category_association = Table(
    "subscription_category_association_table",
    Base.metadata,
    Column("post_category_id", Integer, ForeignKey("post_categories.id")),
    Column("subscription_id", Integer, ForeignKey("subscriptions.id")),
)
