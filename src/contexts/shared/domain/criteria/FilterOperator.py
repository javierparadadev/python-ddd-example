from enum import Enum

from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError


class FilterOperatorValues(Enum):
    EQUALS = '='


class FilterOperator:

    __allowed_values = [e.value for e in FilterOperatorValues]

    def __init__(self, value: str):
        if value not in self.__allowed_values:
            raise ValueObjectValidationError('Filter Operator must be one of {} but {} found.'
                                             .format(self.__allowed_values, value))
        self.value = value
