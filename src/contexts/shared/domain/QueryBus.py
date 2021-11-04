from abc import abstractmethod

from src.contexts.shared.application.Response import Response
from src.contexts.shared.domain.Interface import Interface
from src.contexts.shared.domain.Query import Query


class QueryBus(Interface):

    @abstractmethod
    async def ask(self, query: Query) -> Response:
        raise NotImplementedError()
