from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DEVICE_MANAGEMENT_DB = "postgresql://postgres:postgres@flask_db:5432/postgres"

engine = create_engine(DEVICE_MANAGEMENT_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_device_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()