from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class ValueObjectValidationError(DomainError):

    ERROR_ID = '2266749d-def0-4614-bde7-66e8fcc3b46f'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Attribute validation error.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.get_id(),
        }

    def get_id(self) -> str:
        return ValueObjectValidationError.ERROR_ID
