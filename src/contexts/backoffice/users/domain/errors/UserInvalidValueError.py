from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class UserInvalidValueError(DomainError):

    __ERROR_ID = 'dae09312-2f93-41a0-8798-a5373407e0df'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Invalid value for User found.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.__ERROR_ID,
        }

    def get_id(self) -> str:
        return self.__ERROR_ID
