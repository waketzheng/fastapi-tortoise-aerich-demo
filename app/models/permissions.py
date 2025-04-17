from tortoise import Model, fields


class Permission(Model):
    name = fields.CharField(max_length=20)
