import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DEVICE_MANAGEMENT_DB = os.getenv("DEVICE_DATABASE_URL")

engine = create_engine(DEVICE_MANAGEMENT_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_device_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
