from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class UserAlreadyExistsError(DomainError):

    ERROR_ID = '8eb9e014-76d2-47fc-81f4-c9257095f8c2'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'User already exists.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
