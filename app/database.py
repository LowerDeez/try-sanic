from sanic import Sanic
from sqlalchemy.ext.declarative import declarative_base
from tortoise.contrib.sanic import register_tortoise

from .config import Config

__all__ = (
    'init_database',
    'Base',
)


def init_database(app: Sanic):
    register_tortoise(
        app=app,
        db_url=Config.DATABASE_URL,
        modules={
            'models': ['app.events.schemas', 'app.users.models']
        }
    )


# Use SqlAlchemy base class for all models to be able to make migrations using alembic
Base = declarative_base()
