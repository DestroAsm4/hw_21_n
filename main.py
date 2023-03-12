from shop import Shop
from store import Store
from exceptions import *
from request import Request

store = Store(
    items={
        'печеньки': 10,
        'собачка': 10,
        'елка': 10,
        'пончик': 10,
        'зонт': 10,
        'ноутбук': 10,
    },
)

shop = Shop(
    items={
        'печеньки': 2,
        'собачка': 2,
        'елка': 1,
        'пончик': 3,
        'зонт': 4,
    }
)

storages = {
        'магазин': shop,
        'склад': store,
}

def main():
    print('\nДобрый день\n')

    while True:
        for storege_name in storages:
            print(f'Сейчас в {storege_name}:\n {storages[storege_name].get_items()}')

        user_input = input(
            "Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n "
            "Введите 'стоп', или 'stop', если хотите закончить:\n"
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storages)

        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[request.departure].remove(request.product, request.amount)
            print(f'Курьер забрал {request.amount} {request.product} из {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue

        try:
            storages[request.destination].add(request.product, request.amount)
            print(f'Курьер доставил {request.amount} {request.product} в {request.departure}')
        except LogisticError as error:
            print(error.message)

if __name__ == '__main__':
    main()