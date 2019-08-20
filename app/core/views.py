from sanic.response import json

__all__ = (
    'hello',
)


async def hello(request):
    return json({"hello": "world"})
