import pathlib

from sanic import Sanic

from .core.routes import core_routes

__all__ = (
    'init_routes',
)

PROJECT_PATH = pathlib.Path(__file__).parent


def init_routes(app: Sanic):
    add_route = app.add_route

    for route in core_routes:
        add_route(**route._asdict())

    # added static dir
    app.static(
        '/static/',
        PROJECT_PATH / 'static',
        name='static',
    )
