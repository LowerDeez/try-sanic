""" This module exports the database engine.
Notes:
     Using the scoped_session contextmanager is
     best practice to ensure the session gets closed
     and reduces noise in code by not having to manually
     commit or rollback the db if a exception occurs.
"""
from contextlib import contextmanager
import os
from typing import NamedTuple

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# engine = create_engine(os.environ['DATABASE_URL'])

# Session to be used throughout app.
# Session = sessionmaker(bind=engine)

__all__ = (
    'scoped_session',
    'URLRoute'
)


@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


URLRoute = NamedTuple('URLRoute', [
    ('handler', object),
    ('uri', str)
])
