from abc import abstractmethod
from typing import Any

from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.Interface import Interface


class CommandHandler(Interface):

    @abstractmethod
    async def subscribed_to(self) -> type:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, command: Command) -> Any:
        raise NotImplementedError()
