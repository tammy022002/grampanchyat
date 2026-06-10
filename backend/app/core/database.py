from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from typing import Generator
from app.core.config import settings

# Engine configuration - Using synchronous SQLAlchemy engine with psycopg2
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True, # check connection before usage
    pool_size=10,       # connections to keep open
    max_overflow=20     # extra connections to allow
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# Dependency for FastAPI
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
