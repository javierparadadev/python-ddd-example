from abc import abstractmethod
from typing import Any, NoReturn

from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.Interface import Interface


class CommandHandler(Interface):

    @abstractmethod
    def subscribed_to(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, command: Command) -> NoReturn:
        raise NotImplementedError()
