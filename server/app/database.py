from typing import Annotated, Generator

from fastapi import Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def db_decorator(query_func, exception_message: str = "Database error"):
    def wrapper(*args, **kwargs):
        try:
            return query_func(*args, **kwargs)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=exception_message)

    return wrapper


DatabaseDep = Annotated[Session, Depends(get_db)]
