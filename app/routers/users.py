from fastapi import APIRouter
from pydantic import BaseModel

from app.models.users import User

router = APIRouter()


@router.get("/")
async def get_users():
    objs = await User.all()
    return [{"id": u.id, "name": u.name} for u in objs]


class UserIn(BaseModel):
    name: str


@router.post("/")
async def create_user(data: UserIn):
    obj = await User.create(name=data.name)
    return {"id": obj.pk, "name": obj.name}
