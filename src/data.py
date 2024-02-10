import uuid
from models import Item


class Data():
    def __init__(self):
        self.__items = []

    def get(self):
        return self.__items

    def getById(self, id: str):
        for i in self.__items:
            if i.id == id:
                return i

    def add(self, name: str, quantity: int = 1):
        id = str(uuid.uuid4())
        item = Item(id=id, name=name, quantity=quantity)
        self.__items.append(item)
        return item

    def update(self, id: str, name: str, quantity: int, is_done: bool):
        for i in self.__items:
            if i.id == id:
                i.name = name
                i.quantity = quantity
                i.is_done = is_done
                break
            
    def remove(self, id: str):
        for i in self.__items:
            if i.id == id:
                self.__items.remove(i)
                break
