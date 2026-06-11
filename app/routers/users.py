from fastapi import APIRouter
from pydantic import BaseModel

from app.models.users import User

router = APIRouter()


class UserIn(BaseModel):
    name: str


class UserOut(UserIn):
    id: int


@router.get("/", response_model=list[UserOut])
async def get_users():
    objs = await User.all()
    return [u.model_dump() for u in objs]


@router.post("/", response_model=UserOut)
async def create_user(data: UserIn):
    obj = await User.create(name=data.name)
    return {"id": obj.pk, "name": obj.name}
