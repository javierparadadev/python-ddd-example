from abc import ABC, abstractmethod
from typing import Any, Optional

from src.contexts.shared.domain.Query import Query


class QueryBus(ABC):

    @abstractmethod
    async def ask(self, query: Optional[Query]) -> Any:
        raise NotImplementedError()
