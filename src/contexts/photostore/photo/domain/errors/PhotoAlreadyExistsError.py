from typing import Union, Dict, List

from src.contexts.shared.domain.errors.DomainError import DomainError


class PhotoAlreadyExistsError(DomainError):

    ERROR_ID = 'd71f730d-aa54-4051-a1b2-9092aa41caf1'

    def __init__(self, msg: str = None):
        if msg is None:
            msg = 'Photo already exists.'
        self.message = msg

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'message': self.message,
            'id': self.ERROR_ID,
        }

    def get_id(self) -> str:
        return self.ERROR_ID
