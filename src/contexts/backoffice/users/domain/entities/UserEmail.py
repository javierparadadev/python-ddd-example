from src.contexts.shared.domain.value_obj.ValueObject import ValueObject


class UserEmail(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
