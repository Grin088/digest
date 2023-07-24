import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

user = os.getenv("POSTGRES_USER", "postgres")
password = os.getenv("POSTGRES_PASSWORD", "")
host = os.getenv("POSTGRES_HOST", "postgres_db")
db = os.getenv("POSTGRES_DB", "app")
print(user, password, host, db)

POSTGRES_DATABASE_URL = f"postgresql://{user}:{password}@{host}:5432/{db}"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
