from typing import NoReturn

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.photostore.photo.application.createone.CreatePhotoCommand import CreatePhotoCommand
from src.contexts.photostore.photo.application.createone.PhotoCreator import PhotoCreator
from src.contexts.photostore.photo.domain.entities.PhotoFile import PhotoFile
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreatePhotoCommandHandler(BaseObject, CommandHandler):

    __subscription: str = CreatePhotoCommand.COMMAND_TYPE

    def __init__(self, creator: PhotoCreator):
        self.__creator = creator

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, command: CreatePhotoCommand) -> NoReturn:
        photo_id: PhotoId = PhotoId(command.id)
        photo_name: PhotoName = PhotoName(command.name)
        user_id: UserId = UserId(command.user_id)
        file: PhotoFile = PhotoFile(command.file)

        await self.__creator.run(photo_id, photo_name, user_id, file)


