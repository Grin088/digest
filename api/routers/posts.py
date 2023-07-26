from fastapi import APIRouter
from api.services.posts.posts_service import PostsService

router = APIRouter(prefix="/posts", tags=["posts"])
service = PostsService()


@router.get("/")
def get_all_posts():
    """
    API to get all posts
    :return list[Post]:
    """
    response = service.get_all_posts()
    return response


@router.get("/categories")
def get_posts_categories():
    """
    API to get all categories
    :return list[PostCategory]:
    """
    response = service.get_all_categories()
    return response
