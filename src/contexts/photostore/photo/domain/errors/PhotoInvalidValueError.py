from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class PhotoInvalidValueError(DomainError):

    ERROR_ID = '5bc6edce-4c26-4575-bfdd-4b3a6224440c'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Invalid value for Photo found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
