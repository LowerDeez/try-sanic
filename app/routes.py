from itertools import chain
import pathlib

from sanic import Sanic

from .core.routes import core_routes
from .events.routes import event_routes
from .users.routes import user_routes

__all__ = (
    'init_routes',
)

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app: Sanic):
    add_route = app.add_route

    all_routes = chain(
        core_routes,
        event_routes,
        user_routes
    )

    for route in all_routes:
        add_route(**route._asdict())

    # added static dir
    app.static(
        '/static/',
        PROJECT_PATH / 'static',
        name='static',
    )
