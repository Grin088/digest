from sqlalchemy import Column, Integer, String, ForeignKey, Text, BigInteger, Numeric
from sqlalchemy.orm import relationship, backref
from api.db.base_class import Base


class PostCategory(Base):
    __tablename__ = "post_categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True)
    parent_id = Column(Integer, ForeignKey("post_categories.id"))

    children = relationship(
        "PostCategory",
        backref=backref("parent", remote_side=[id]),
        cascade="save-update",
    )
    posts = relationship(
        "Post", back_populates="post_category", cascade="all, delete-orphan"
    )
    subscriptions = relationship(
        "Subscription",
        secondary="subscription_category_association_table",
        back_populates="post_categories",
        cascade="save-update",
    )


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    post_category_id = Column(Integer, ForeignKey("post_categories.id"))
    name = Column(String)
    text = Column(Text)
    rating = Column(Numeric)
    views = Column(BigInteger)

    post_category = relationship(
        "PostCategory",
        back_populates="posts",
        foreign_keys=[post_category_id],
        cascade="save-update",
    )
