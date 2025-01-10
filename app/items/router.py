from fastapi import APIRouter
from typing import Union
from .schemas import Item

router = APIRouter(prefix='/items', tags=['items'])


@router.post('/new_item')
async def new_item(item: Item):
    ...  # добавить добавление итема в базу
    return item


@router.get("/get_item/{item_id}")
async def get_item(item_id: int, q: Union[str, None] = None):
    ...  # добавить выборку данных из базы
    return {"item_id": item_id, "q": q}
