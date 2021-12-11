from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class PhotoRegistryAlreadyExistsError(DomainError):

    ERROR_ID = '228d3d16-97a5-4163-97fa-e4db802b2a81'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Photo registry already exists.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
