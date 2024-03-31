from pydantic import BaseModel


class Message(BaseModel):
    text: str


print(Message.schema())
print(Message.model_json_schema())
