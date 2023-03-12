from abstract_storage import AbstractStorage
from exceptions import NotEnouthProduct, NotEnouthSpace, UnknownProduct


class BaseStorage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:

        if self.get_free_space() < amount:
            raise NotEnouthSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        if name not in self.__items:
            raise UnknownProduct

        if self.__items[name] < amount:
            raise NotEnouthProduct



        self.__items[name] -= amount
        if self.__items[name] == 0:
            del self.__items[name]

    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)