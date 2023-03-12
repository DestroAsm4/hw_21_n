class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnouthSpace(LogisticError):
    message = 'Недостаточно места на складе'


class NotEnouthProduct(LogisticError):
    message = 'Недостаточно товара на складе'


class UnknownProduct(LogisticError):
    message = 'Неизвестный товар'


class TooManyDifferentProduct(LogisticError):
    message = 'Слишком много разных товаров'


class InvailidRequest(RequestError):
    message = 'Неправильный запрос. Попробуйте снова'


class InvailidStorageNmae(RequestError):
    message = 'Выбран несуществующий склад'