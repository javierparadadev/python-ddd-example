from src.contexts.shared.domain.value_obj.ValueObject import ValueObject


class UserId(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
