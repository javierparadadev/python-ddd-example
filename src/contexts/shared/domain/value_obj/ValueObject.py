from typing import Any


class ValueObject:

    def __init__(self, value: Any):
        self.__value = value

    def value(self):
        return self.__value
