from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class PhotoTag(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
