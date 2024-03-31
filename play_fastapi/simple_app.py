from typing import Generic, List, Optional, TypeVar

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic.generics import GenericModel

app = FastAPI()


messages = []


class BaseMetaModel(BaseModel):
    code: int = 200
    message: str = "ok"


CustomModel = TypeVar("CustomModel")


class StandardResponseModel(GenericModel, Generic[CustomModel]):
    meta: BaseMetaModel = {"code": 200, "message": "ok"}
    content: Optional[CustomModel]


class Item(BaseModel):
    name: str


class Message(BaseModel):
    text: str
    item: Item


@app.post("/messages/", response_model=Message)
async def create_message(message: Message):
    messages.append(message)
    return message


@app.get("/messages/")
async def get_messages() -> StandardResponseModel[Message]:
    return StandardResponseModel(content=Message())
