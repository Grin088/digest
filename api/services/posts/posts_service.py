from typing import List

from api.db.session import SessionLocal
from api.db.models.post import Post, PostCategory


class PostsService:
    """Claas ro handle post endpoints"""

    def get_all_posts(self) -> List[Post]:
        """Method to get all posts"""
        with SessionLocal() as session:
            posts = session.query(Post).all()
            return posts

    def get_all_categories(self) -> List[PostCategory]:
        """Method to get all categories"""
        with SessionLocal() as session:
            categories = session.query(PostCategory).all()
            return categories
