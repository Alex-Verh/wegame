from typing import Any, List, Sequence, Type

from app.models.base import Base
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable


class DBSessionMixin:
    """Provides instance of database session."""

    def __init__(self, db_session: Session) -> None:
        self.db: Session = db_session


class BaseService(DBSessionMixin):
    """Base class for application services."""


class BaseDataManager(DBSessionMixin):
    """Base data manager class responsible for operations over database."""

    def get_one_by_pk(self, model: Type[Base], id: int) -> Any:  # type: ignore
        return self.db.get(model, id)

    def get_one_by_kwargs(self, model: Type[Base], **kwargs: Any) -> Any:  # type: ignore
        return self.db.query(model).filter_by(**kwargs).first()

    def get_all(self, model: Type[Base], skip: int = 0, limit: int = 100) -> List[Any]:  # type: ignore
        return self.db.query(model).offset(skip).limit(limit).all()

    def get_all_by_kwargs(self, model: Type[Base], **kwargs: Any) -> List[Any]:  # type: ignore
        return self.db.query(model).filter_by(**kwargs).all()

    def add_one(self, instance: Any) -> Any:
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def add_all(self, instances: Sequence[Any]) -> None:
        self.db.add_all(instances)
        self.db.commit()

    def update_one(self, instance: Any, **kwargs: Any) -> Any:
        for key, value in kwargs.items():
            setattr(instance, key, value)

        self.db.commit()
        self.db.refresh(instance)
        return instance

    def update_one_by_pk(self, model: Type[Base], id: int, **kwargs: Any) -> None:  # type: ignore
        self.db.query(model).filter_by(id=id).update(kwargs)
        self.db.commit()

    def delete_one(self, instance: Any) -> None:
        self.db.delete(instance)
        self.db.commit()

    def delete_one_by_pk(self, model: Type[Base], id: int) -> None:  # type: ignore
        self.db.query(model).filter_by(id=id).delete()
        self.db.commit()

    def delete_one_by_kwargs(self, model: Type[Base], **kwargs: Any) -> None:  # type: ignore
        self.db.query(model).filter_by(**kwargs).delete()
        self.db.commit()
