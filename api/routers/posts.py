from fastapi import APIRouter
from api.services.posts.posts_service import PostsService as Service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
def get_all_posts():
    response = Service().get_all_posts()
    return response


@router.get("/categories")
def get_posts_categories():
    response = Service().get_all_categories()
    return response
