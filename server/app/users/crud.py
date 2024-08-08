from sqlalchemy.orm import Session

from ..security import get_password_hash
from . import models, schemas


def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).get(user_id)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(**user.model_dump(exclude=("language_ids", "platform_ids")))
    db_user.password = get_password_hash(user.password)
    for language_id in user.language_ids:
        db_language = models.UserLanguage(user_id=user.id, language_id=language_id)
        db.add(db_language)
    for platform_id in user.platform_ids:
        db_platform = models.UserPlatform(user_id=user.id, platform_id=platform_id)
        db.add(db_platform)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(
    db: Session, db_user: models.User, user: schemas.UserUpdate
) -> models.User:
    user_data = user.model_dump(exclude_unset=True)
    if "password" in user_data:
        user_data["password"] = get_password_hash(user_data["password"])

    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    res = db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return res
