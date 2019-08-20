from typing import NamedTuple

URLRoute = NamedTuple('URLRoute', [
    ('handler', object),
    ('uri', str)
])
