from sqlalchemy import (
    Column,
    String,
    Text,
    Integer
)

from app.database import Base

__all__ = (
    'Tournament',
)


class Tournament(Base):
    __tablename__ = 'tournament'

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True
    )
    name = Column(
        String(255),
        nullable=False
    )
    description = Column(
        Text(),
    )

    def __str__(self):
        return self.name
