from .views import UserView
from app.utils import URLRoute


user_routes = [
    URLRoute(handler=UserView.as_view(), uri='/users')
]
