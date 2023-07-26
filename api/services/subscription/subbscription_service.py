from typing import List

from fastapi import HTTPException
from sqlalchemy import desc

from api.db.models.post import PostCategory
from api.db.models.subscription import Subscription
from api.db.session import SessionLocal
from api.services.exceptions.utils import check_object
from api.celery_tasks.tasks import update_create_user_digest
from api.db.models.digest import Digest
from api.db.models.post import Post


class SubscriptionService:
    """Service to handle requests from subscription endpoints"""

    def add_subscription(self, user_id, category_id) -> Subscription:
        """Method to add subscription for user"""
        with SessionLocal() as session:
            subscription = (
                session.query(Subscription).filter_by(user_id=user_id).first()
            )

            if not subscription:
                subscription = Subscription(user_id=user_id)
                session.add(subscription)
                session.commit()
                session.refresh(subscription)

            post_category = check_object(
                obj=PostCategory, session=session, obj_exist=True, id=category_id
            )
            if post_category in subscription.post_categories:
                raise HTTPException(
                    status_code=400,
                    detail=f"User with id:{user_id} already subscribe on category id:{category_id}",
                )

            child_categories = (
                session.query(PostCategory).filter_by(parent_id=category_id).all()
            )
            subscription.post_categories.append(post_category)
            subscription.post_categories.extend(child_categories)
            session.commit()

            update_create_user_digest.apply_async(args=(user_id,))

            return subscription

    def get_subscriptions(self, user_id) -> List[PostCategory]:
        """Method to get all subscriptions categories for user"""
        with SessionLocal() as session:
            subscription = check_object(
                obj=Subscription, session=session, obj_exist=True, user_id=user_id
            )
            return subscription.post_categories
