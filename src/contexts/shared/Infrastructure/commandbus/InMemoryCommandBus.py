from typing import Any, Dict

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.CommandHandler import CommandHandler
from src.contexts.shared.domain.errors.CommandNoRegisteredError import CommandNotRegisteredError


class InMemoryCommandBus(BaseObject, CommandBus):

    def __init__(self, *handlers: CommandHandler):
        handler_mapping = {}
        for handler in handlers:
            handler_mapping[handler.subscribed_to()] = handler
        self.__handler_mapping: Dict[str, CommandHandler] = handler_mapping

    def __search(self, command_name: str):
        if command_name not in self.__handler_mapping:
            raise CommandNotRegisteredError()
        return self.__handler_mapping[command_name]

    async def dispatch(self, command: Command) -> Any:
        query_type: str = command.get_command_type_name()
        handler = self.__search(query_type)
        return await handler.handle(command)
