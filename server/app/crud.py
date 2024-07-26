from sqlalchemy.orm import Session

from . import models, schemas
from .security import get_password_hash


def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(**user.model_dump(exclude=("language_ids", "platform_ids")))
    db_user.password = get_password_hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_game(db: Session, game_id: int) -> models.Game | None:
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_games(db: Session, skip: int = 0, limit: int = 100) -> list[models.Game]:
    return db.query(models.Game).offset(skip).limit(limit).all()


def create_game(db: Session, game: schemas.GameCreate) -> models.Game:
    db_game = models.Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def delete_game(db: Session, game_id: int) -> bool:
    res = db.query(models.Game).filter(models.Game.id == game_id).delete()
    db.commit()
    return res


def get_language(db: Session, language_id: int) -> models.Language | None:
    return db.query(models.Language).filter(models.Language.id == language_id).first()


def get_languages(
    db: Session, skip: int = 0, limit: int = 100
) -> list[models.Language]:
    return db.query(models.Language).offset(skip).limit(limit).all()


def create_language(db: Session, language: schemas.LanguageCreate) -> models.Language:
    db_language = models.Language(**language.model_dump())
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language


def delete_language(db: Session, language_id: int) -> int:
    res = db.query(models.Language).filter(models.Language.id == language_id).delete()
    db.commit()
    return res


def get_platform(db: Session, platform_id: int) -> models.Platform | None:
    return db.query(models.Platform).filter(models.Platform.id == platform_id).first()


def get_platforms(
    db: Session, skip: int = 0, limit: int = 100
) -> list[models.Platform]:
    return db.query(models.Platform).offset(skip).limit(limit).all()


def create_platform(db: Session, platform: schemas.PlatformCreate) -> models.Platform:
    db_platform = models.Platform(**platform.model_dump())
    db.add(db_platform)
    db.commit()
    db.refresh(db_platform)
    return db_platform


def delete_platform(db: Session, platform_id: int) -> int:
    res = db.query(models.Platform).filter(models.Platform.id == platform_id).delete()
    db.commit()
    return res


def get_auth_session(
    db: Session, user_id: int, ip_address: str, user_agent: str
) -> models.AuthSession | None:
    return (
        db.query(models.AuthSession)
        .filter_by(user_id=user_id, ip_address=ip_address, user_agent=user_agent)
        .first()
    )


def get_auth_session_by_refresh_token(
    db: Session, refresh_token: str
) -> models.AuthSession | None:
    return db.query(models.AuthSession).filter_by(refresh_token=refresh_token).first()


def create_auth_session(
    db: Session, auth_session: schemas.AuthSession
) -> models.AuthSession:
    db_auth_session = models.AuthSession(**auth_session.model_dump())
    db.add(db_auth_session)
    db.commit()
    db.refresh(db_auth_session)
    return db_auth_session


def update_auth_session(
    db: Session, db_auth_session: models.AuthSession, refresh_token: str
) -> models.AuthSession:

    db_auth_session.refresh_token = refresh_token
    db.commit()
    db.refresh(db_auth_session)

    return db_auth_session


def delete_auth_session(
    db: Session, user_id: int, ip_address: str, user_agent: str
) -> int:
    res = (
        db.query(models.AuthSession)
        .filter_by(user_id=user_id, ip_address=ip_address, user_agent=user_agent)
        .delete()
    )
    db.commit()
    return res
