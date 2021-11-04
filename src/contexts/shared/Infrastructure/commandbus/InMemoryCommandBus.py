from typing import Any, Dict

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.CommandHandler import CommandHandler
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.errors.CommandNoRegisteredError import CommandNotRegisteredError
from src.contexts.shared.domain.errors.QueryNoRegisteredError import QueryNotRegisteredError


class InMemoryCommandBus(BaseObject, CommandBus):

    def __init__(self):
        self.__handler_mapping: Dict[str, CommandHandler] = {}

    def __search(self, command_name: str):
        if command_name not in self.__handler_mapping:
            raise CommandNotRegisteredError()
        return self.__handler_mapping[command_name]

    async def dispatch(self, command: Command) -> Any:
        query_type: str = command.get_command_type_name()
        handler = self.__search(query_type)
        return await handler.handle(command)
