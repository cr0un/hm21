from typing import Dict, Tuple
from utils.Storage import Storage



class Request:
    def __init__(self, request: str, storages: Dict[str, Storage]):
        # Парсим запрос на количество товара, его название, откуда и куда нужно доставить
        self._quantity, self._product, self._from, self._to = self._parse_request(request)
        # Получаем объекты складов из словаря, используя их имена
        self._from_storage = storages.get(self._from)
        self._to_storage = storages.get(self._to)

        if not self._from_storage or not self._to_storage:
            # Если один из складов не найден, выбрасываем исключение
            raise ValueError('Неверное название склада')

    def _parse_request(self, request: str) -> Tuple[int, str, str, str]:
        # Разбиваем запрос на части и проверяем формат
        parts = request.split()
        if len(parts) != 7 or not parts[1].isdigit() or parts[3] != 'из' or parts[5] != 'в':
            raise ValueError('Неверный формат запроса')
        # Возвращаем кортеж из количества товара, названия товара, склада отправителя и склада получателя
        return int(parts[1]), parts[2], parts[4], parts[6]

    def get_quantity(self):
        return self._quantity

    def get_product(self):
        return self._product

    def get_from(self):
        return self._from

    def get_to(self):
        return self._to

    def get_from_storage(self):
        return self._from_storage

    def get_to_storage(self):
        return self._to_storage