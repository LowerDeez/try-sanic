from gino.ext.sanic import Gino
from sanic import Sanic

__all__ = (
    'DATABASE',
    'init_database'
)


DATABASE = Gino()


def init_database(app: Sanic):
    DATABASE.init_app(app)
