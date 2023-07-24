from api.db.session import SessionLocal
from api.db.models.digest import Digest
from api.services.exceptions.utils import check_object


class DigestService:

    def get_user_digest(self, user_id) -> dict:
        """Method to get digest for user"""
        with SessionLocal() as session:
            user_digest = check_object(obj=Digest, session=session, obj_exist=True, user_id=user_id)
            response = {"user": user_digest.user_id, "posts": user_digest.posts}
            return response
