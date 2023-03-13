from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, capacity: int):
        self._items = {}  # словарь товаров на складе
        self._capacity = capacity  # вместимость склада

    @abstractmethod
    def add(self, name: str, quantity: int):
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int):
        pass

    def get_free_space(self):
        return self._capacity - sum(self._items.values())  # свободное место на складе

    def get_items(self):
        return self._items.copy()  # копия словаря товаров на складе

    def get_unique_items_count(self):
        return len(self._items)  # количество уникальных товаров на складе

    def get_capacity(self):
        return self._capacity  # вместимость склада

    def set_capacity(self, capacity: int):
        self._capacity = capacity  # установка вместимости склада

    def get_items_count(self, name: str):
        return self._items.get(name, 0)  # количество товара с заданным именем на складе