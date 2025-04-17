from tortoise import Model, fields


class Group(Model):
    name = fields.CharField(max_length=10)


class User(Model):
    name = fields.CharField(max_length=20)
