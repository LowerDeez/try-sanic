from typing import NamedTuple

__all__ = (
    'URLRoute',
)

URLRoute = NamedTuple('URLRoute', [
    ('handler', object),
    ('uri', str)
])
