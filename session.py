from pydantic.typing import Generator, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:  # new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


session_maker = sessionmaker()
session_maker.configure(bind=engine)


class DatabaseSession:
    def __init__(self, session: Optional[Session] = None):
        self.session = session_maker() if session is None else session

    def __enter__(self) -> Session:
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
            self.session.close()
            raise exc_val

        self.session.commit()
        self.session.close()
