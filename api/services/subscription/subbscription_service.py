from api.db.models.post import PostCategory
from api.db.models.subscription import Subscription
from api.db.session import SessionLocal
from api.services.exceptions.utils import check_object
from api.celery_tasks.tasks import update_create_user_digest


class SubscriptionService:

    def add_subscription(self, user_id, category_id):
        with SessionLocal() as session:
            subscription = check_object(obj=Subscription, session=session, obj_exist=True, user_id=user_id)
            post_category = check_object(obj=PostCategory, session=session, obj_exist=True, id=category_id)
            print(post_category)
            subscription.post_categories.append(post_category)
            session.commit()

            update_create_user_digest.apply_async(args=(user_id,))

            return subscription

    def get_subscriptions(self, user_id):
        with SessionLocal() as session:
            subscription = check_object(obj=Subscription, session=session, obj_exist=True, user_id=user_id)
            return subscription.post_categories
