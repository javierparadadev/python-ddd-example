from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class OrderDirectionValues(Enum):
    ASC = 'asc'
    DESC = 'desc'


class OrderDirection:

    __allowed_values = [e.value for e in OrderDirectionValues]

    def __init__(self, order_dir: str):
        if order_dir not in self.__allowed_values:
            raise ValueObjectValidationError('Order direction must be one of {} but {} found.'
                                             .format(self.__allowed_values, order_dir))
        self.value = order_dir
