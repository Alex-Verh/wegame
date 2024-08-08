from sqlalchemy.orm import Session

from . import models, schemas


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
