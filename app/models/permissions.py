from ._base import BaseModel, fields


class Permission(BaseModel):
    name = fields.CharField(max_length=20)
