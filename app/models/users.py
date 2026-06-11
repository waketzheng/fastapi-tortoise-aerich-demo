from ._base import BaseModel, fields


class Group(BaseModel):
    name = fields.CharField(max_length=10)


class User(BaseModel):
    name = fields.CharField(max_length=20)
