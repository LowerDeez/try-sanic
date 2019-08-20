import os

from sanic import Sanic

__all__ = (
    'Config',
    'init_config'
)


class Config:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DB_HOST = os.environ.get('DB_HOST')
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')


def init_config(app: Sanic, config: str = 'app.config.Config'):
    app.config.from_object(config)
