from typing import Dict
from utils.Storage import Storage
from utils.Request import Request
from utils.Shop import Shop
from utils.Warehouse import Warehouse


# Создаем склады и магазин
warehouse = Warehouse(20)
warehouse.add('печеньки', 3)
warehouse.add('собачки', 2)
warehouse.add('коробки', 5)
# warehouse.add('мышки', 5)
# warehouse.add('вилки', 5)

shop = Shop()
shop.add('собачки', 2)
shop.add('коробки', 5)
shop.add('ножи', 5)

# Создаем словарь складов
storages: Dict[str, Storage] = {'склад': warehouse, 'магазин': shop}

def main():
    # Основной цикл программы
    while True:
        # Выводим сообщение о доступных товарах на складе
        print(f'На складе есть:')
        items = warehouse.get_items()
        for name, quantity in items.items():
            print(f'{name}: {quantity}')

        # Выводим сообщение о доступных товарах в магазине
        print(f'В магазине есть:')
        items = shop.get_items()
        for name, quantity in items.items():
            print(f'{name}: {quantity}')

        # Выводим приглашение для ввода команды
        print('Введите команду в формате: "Доставить <количество> <товар> из <откуда> в <куда>"')
        command = input('> ')

        # Если пользователь ввел пустую строку, завершаем цикл
        if not command:
            print('До свидания!')
            break

        try:
            # Создаем запрос
            request = Request(command, storages)

            # Проверяем, достаточно ли товаров на складе для перемещения
            if request.get_from_storage().get_items_count(request.get_product()) < request.get_quantity():
                print(f'Не хватает товара "{request.get_product()}" на складе "{request.get_from()}"')
                continue

            # Перемещаем товары
            request.get_from_storage().remove(request.get_product(), request.get_quantity())
            request.get_to_storage().add(request.get_product(), request.get_quantity())

            # Выводим сообщение о доставке
            print(f'Курьер забирает {request.get_quantity()} {request.get_product()} из {request.get_from()}')
            print(f'Курьер везет {request.get_quantity()} {request.get_product()} из {request.get_from()} в {request.get_to()}')
            print(f'Курьер доставил {request.get_quantity()} {request.get_product()} в {request.get_to()}')

        except ValueError as e:
            print(f'Ошибка: {str(e)}')


if __name__ == "__main__":
    main()