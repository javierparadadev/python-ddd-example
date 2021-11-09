from abc import abstractmethod
from typing import Any

from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.Query import Query


class QueryHandler(Interface):

    @abstractmethod
    def subscribed_to(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, query: Query) -> Any:
        raise NotImplementedError()
