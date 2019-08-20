import os
from sanic import Sanic

from .config import init_config
from .database import init_database
from .routes import init_routes


def create_app(host: str = "0.0.0.0", port: int = 8000):
    app = Sanic(__name__)

    init_config(app)
    init_routes(app)
    init_database(app)

    # Register Blueprints/Views.
    # from app.controllers.users import UserController
    # app.add_route(UserController.as_view(), '/api/user')

    app.go_fast(
        debug=True,
        workers=os.cpu_count(),
        host=host,
        port=port
    )

    return app
