from fastapi import APIRouter
from api.services.subscription.subbscription_service import SubscriptionService

router = APIRouter(prefix="/subscription", tags=["subscriptions"])
service = SubscriptionService()


@router.post("/")
def add_subscribe(user_id: int, category_id: int):
    """Add subscribe for user"""
    service.add_subscription(user_id, category_id)
    return {200: f"Subscription {category_id} was added for user {user_id}, worker start create digest"}


@router.get("/")
def get_subscriptions(user_id: int):
    """Add all subscribers"""
    result = service.get_subscriptions(user_id)
    return result
