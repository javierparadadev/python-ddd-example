from typing import Any, NoReturn

from src.contexts.backoffice.users.application.commands.CreateUserCommand import CreateUserCommand
from src.contexts.backoffice.users.application.usecases.UserCreator import UserCreator
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.CommandHandler import CommandHandler


class CreateUserCommandHandler(BaseObject, CommandHandler):

    __subscription: str = CreateUserCommand.COMMAND_TYPE

    def __init__(self, creator: UserCreator):
        self.__creator = creator

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, command: CreateUserCommand) -> NoReturn:
        user_id: UserId = UserId(command.id)
        user_name: UserName = UserName(command.name)
        await self.__creator.run(user_id, user_name)


