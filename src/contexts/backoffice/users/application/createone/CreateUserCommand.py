from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command


class CreatePhotoCommand(BaseObject, Command):

    COMMAND_TYPE: str = 'createone-photo'

    def __init__(self, photo_id: str, name: str, user_id: str, file: bytes):
        self.id = photo_id
        self.name = name
        self.user_id = user_id
        self.file = file

    def get_command_type_name(self) -> str:
        return self.COMMAND_TYPE
