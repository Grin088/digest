from fastapi import APIRouter
from api.services.digest.digest_service import DigestService as Service


router = APIRouter(prefix="/digest", tags=["digests"])
service = Service()


@router.get("/")
async def get_digest(user_id: int):
    result = service.get_user_digest(user_id)
    return result
