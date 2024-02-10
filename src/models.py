from pydantic import BaseModel

class Item(BaseModel):
    id: str
    name: str
    quantity: int
    is_done: bool = False

class AddItemRequest(BaseModel):
    name: str
    quantity: int = 1

class UpdateItemRequest(BaseModel):
    name: str
    quantity: int
    is_done: bool