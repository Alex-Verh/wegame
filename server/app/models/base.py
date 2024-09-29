from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


from app.models import applications, auth, games, languages, parties, platforms, users
