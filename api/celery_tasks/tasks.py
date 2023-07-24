import os
from sqlalchemy import desc
from celery import Celery

from api.db.session import SessionLocal
from api.db.models.post import Post, PostCategory
from api.db.models.subscription import Subscription
from api.db.models.digest import Digest
from api.logger.logger_main import logger


RABBITMQ_HOST = os.getenv("RABBITMQ_DEFAULT_HOST", "rabbitmq")
app = Celery('tasks', broker=f'pyamqp://{RABBITMQ_HOST}/vhost')


@app.task(name='tasks.update_create_user_digest')
def update_create_user_digest(user_id):
    """Func to create digest for subscriber"""

    with SessionLocal() as session:
        try:
            subscription = (
                session.query(Subscription).filter_by(user_id=user_id).first()
            )
            subscription_categories = [
                category.id for category in subscription.post_categories
            ]
            child_subscriptions_categories = (
                session.query(PostCategory)
                .filter(PostCategory.parent_id.in_(subscription_categories))
                .all()
            )
            child_categories = [
                category.id for category in child_subscriptions_categories
            ]
            subscription_categories.extend(child_categories)
            posts = (
                session.query(Post)
                .filter(Post.post_category_id.in_(subscription_categories))
                .order_by(desc(Post.rating), desc(Post.views))
                .all()
            )

            digest_posts = [
                {
                    post.post_category.name: {
                        "id": post.post_category.id,
                        "name": post.name,
                        "text": post.text,
                        "rating": float(post.rating),
                        "views": post.views,
                    }
                }
                for post in posts if post.rating >= 3
            ]

            user_digest = session.query(Digest).filter_by(user_id=user_id).first()
            # для наглядности результата отключил сериализацию
            # jason_digest = json.dumps(digest_posts, indent=4)
            if not user_digest:
                user_digest = Digest(user_id=user_id, posts=digest_posts)
                session.add(user_digest)

            else:
                user_digest.posts = digest_posts

            session.commit()

        except Exception as e:
            logger.error(e, exc_info=True)
