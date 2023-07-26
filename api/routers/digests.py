from fastapi import APIRouter
from api.services.digest.digest_service import DigestService as Service


router = APIRouter(prefix="/digest", tags=["digests"])
digest_service = Service()


@router.get("/")
async def get_digest(user_id: int):
    """
    API to get digest with posts for user
    :param user_id:
    :return Digest:
    """
    result = digest_service.get_user_digest(user_id)
    return result
