from .views import hello
from app.utils import URLRoute

__all__ = (
    'core_routes',
)

core_routes = [
    URLRoute(handler=hello, uri='/')
]
