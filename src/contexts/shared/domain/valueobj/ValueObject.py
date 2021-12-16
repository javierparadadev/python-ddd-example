from typing import Any


class ValueObject:

    def __init__(self, value: Any):
        self._value = value

    def value(self):
        return self._value
