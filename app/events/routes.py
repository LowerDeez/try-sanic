from .views import tournaments
from app.utils import URLRoute

__all__ = (
    'event_routes',
)


event_routes = [
    URLRoute(handler=tournaments, uri='/tournaments')
]
