from fastapi import APIRouter
from typing import Union
from .schemas import User

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/new_user')
async def new_user(user: User):
    ...  # добавить добавление юзера в базу
    return User


@router.get("/get_user/{user_id}")
async def get_user(user_id: int, q: Union[str, None] = None):
    ...  # добавить выборку данных из базы
    return {"user_id": user_id, "q": q}
