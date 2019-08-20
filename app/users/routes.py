from .views import UserView
from app.utils import URLRoute

__all__ = (
    'user_routes',
)


user_routes = [
    URLRoute(handler=UserView.as_view(), uri='/users')
]
