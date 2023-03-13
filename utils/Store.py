from utils.Storage import Storage


class Store(Storage):
    def __init__(self, capacity: int = 100):
        super().__init__(capacity)

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise ValueError('Нет свободного места в магазине')
        self._items[name] = self._items.get(name, 0) + quantity

    def remove(self, name: str, quantity: int):
        self._items[name] = max(0, self._items.get(name, 0) - quantity)