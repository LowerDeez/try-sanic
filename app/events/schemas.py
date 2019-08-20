from tortoise import Model, fields

__all__ = (
    'TournamentSchema',
)


class TournamentSchema(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    class Meta:
        table = "tournament"

    def __str__(self):
        return self.name
