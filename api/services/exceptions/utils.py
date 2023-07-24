from api.db.session import SessionLocal
from api.services.exceptions import DataBaseObjectException
from sqlalchemy.ext.declarative import declarative_base


def check_object(
    obj: declarative_base, session: SessionLocal, obj_exist=None, obj_not_exist=None, **kwargs
) -> declarative_base:
    session = session
    obj_instance = session.query(obj).filter_by(**kwargs).first()

    if not obj_instance and obj_exist:
        raise DataBaseObjectException(
            status_code=404,
            content={"detail": f"{obj.__name__} with {kwargs} does not exist"},
        )
    elif obj_instance and obj_not_exist:
        raise DataBaseObjectException(
            status_code=400,
            content={"detail": f"{obj.__name__} with {kwargs} already exists"},
        )
    return obj_instance
