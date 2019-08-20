from sanic.response import json

from app.events.schemas import TournamentSchema

__all__ = (
    'tournaments',
)


async def tournaments(request):
    objs = await TournamentSchema.all()
    if objs:
        return json({"tournaments": [str(obj) for obj in objs]})
    return json({})
