from abc import abstractmethod
from typing import Any, Optional

from src.contexts.shared.domain.Command import Command
from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.Query import Query


class CommandBus(Interface):

    @abstractmethod
    async def dispatch(self, command: Command) -> Any:
        raise NotImplementedError()
