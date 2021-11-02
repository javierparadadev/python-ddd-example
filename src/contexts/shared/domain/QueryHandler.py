from abc import ABC, abstractmethod
from typing import Optional, Any

from src.contexts.shared.domain.Query import Query


class QueryBus(ABC):

    @abstractmethod
    async def subscribed_to(self) -> type:
        raise NotImplementedError()

    @abstractmethod
    async def handle(self, query: Optional[Query]) -> Any:
        raise NotImplementedError()
