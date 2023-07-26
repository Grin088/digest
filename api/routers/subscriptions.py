from fastapi import APIRouter
from api.services.subscription.subbscription_service import SubscriptionService

router = APIRouter(prefix="/subscription", tags=["subscriptions"])
subscription_service = SubscriptionService()


@router.post("/")
def add_subscribe(user_id: int, category_id: int):
    """
    API to add post category to user subscription
    :param user_id:
    :param category_id:
    :return:
    """
    subscription_service.add_subscription(user_id, category_id)
    return {
        200: f"Subscription {category_id} was added for user {user_id}, worker start create digest"
    }


@router.get("/")
def get_subscriptions(user_id: int):
    """
    API to get all subscriptions for user
    :param user_id:
    :return list[Subscription]:
    """
    result = subscription_service.get_subscriptions(user_id)
    return result
