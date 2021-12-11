from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class PhotoFile(ValueObject):

    def __init__(self, content: bytes):
        super().__init__(content)
