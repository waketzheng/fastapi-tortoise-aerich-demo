from typing import Any

from tortoise import Model, fields


class BaseModel(Model):
    id = fields.IntField(primary_key=True)

    class Meta:
        abstract = True

    def model_dump(self) -> dict[str, Any]:
        fields = self._meta.db_fields
        return {f: getattr(self, f) for f in fields}
