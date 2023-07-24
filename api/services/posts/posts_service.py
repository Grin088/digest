from api.db.session import SessionLocal
from api.db.models.post import Post, PostCategory


class PostsService:

    def get_all_posts(self):
        with SessionLocal() as session:
            posts = session.query(Post).all()
            return posts

    def get_all_categories(self):
        with SessionLocal() as session:
            categories = session.query(PostCategory).all()
            return categories
