from utils.Storage import Storage


class Shop(Storage):
    def __init__(self, capacity: int = 20):
        super().__init__(capacity)
        self._max_unique_items_count = 5  # максимальное количество уникальных товаров в магазине

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise ValueError('Нет свободного места в магазине')
        if len(self._items) >= self._max_unique_items_count and name not in self._items:
            raise ValueError('Слишком много разных товаров в магазине')
        self._items[name] = self._items.get(name, 0) + quantity

    def remove(self, name: str, quantity: int):
        self._items[name] = max(0, self._items.get(name, 0) - quantity)