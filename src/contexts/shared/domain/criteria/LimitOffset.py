from typing import Any


class LimitOffset:

    def __init__(self, value: Any):
        if isinstance(value, str):
            value = int(value)
        self.value = value
