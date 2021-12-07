from typing import Any


class UpperLimit:

    def __init__(self, value: Any):
        if isinstance(value, str):
            value = int(value)
        self.value = value
