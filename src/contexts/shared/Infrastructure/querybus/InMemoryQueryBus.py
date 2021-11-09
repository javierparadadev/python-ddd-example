from typing import Any, Dict, List

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.errors.QueryNoRegisteredError import QueryNotRegisteredError


class InMemoryQueryBus(BaseObject, QueryBus):

    def __init__(self, *handlers: QueryHandler):
        handler_mapping = {}
        for handler in handlers:
            handler_mapping[handler.subscribed_to()] = handler
        self.__handler_mapping: Dict[str, QueryHandler] = handler_mapping

    def __search(self, query_name: str):
        if query_name not in self.__handler_mapping:
            raise QueryNotRegisteredError()
        return self.__handler_mapping[query_name]

    async def ask(self, query: Query) -> Any:
        query_type: str = query.get_query_type_name()
        handler = self.__search(query_type)
        return await handler.handle(query)
