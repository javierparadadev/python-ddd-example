from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class PhotoRegistryInvalidValueError(DomainError):

    ERROR_ID = 'b363da63-6dbc-4af0-8a94-cbcec204f4fc'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Invalid value for photo registry found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
