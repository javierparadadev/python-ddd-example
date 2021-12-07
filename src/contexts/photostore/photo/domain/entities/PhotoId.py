from src.contexts.shared.domain.errors.ValueObjectValidationError import ValueObjectValidationError
from src.contexts.shared.domain.valueobj.ValueObject import ValueObject
from src.utils.Uuid import Uuid


class PhotoId(ValueObject):

    def __init__(self, value: str):
        super().__init__(value)
        if not Uuid.is_valid_uuid(value):
            raise ValueObjectValidationError(f'PhotoId must be UUID V4. <{value}> found.')
