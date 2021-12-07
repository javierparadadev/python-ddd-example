from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class CommandNotRegisteredError(DomainError):

    ERROR_ID = 'feba3dde-5a79-4aab-8770-33a2451302d0'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Command not registered.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.get_id(),
        }

    def get_id(self) -> str:
        return CommandNotRegisteredError.ERROR_ID
