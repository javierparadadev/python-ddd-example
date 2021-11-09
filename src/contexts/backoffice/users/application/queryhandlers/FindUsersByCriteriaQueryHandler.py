from typing import List

from src.contexts.backoffice.users.application.queries.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.backoffice.users.application.usecases.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.shared.domain.QueryBus import QueryBus
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindUsersByCriteriaQueryHandler(QueryHandler):

    __subscription: str = FindUsersByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: UsersByCriteriaFinder):
        self.__finder = finder

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, query: FindUsersByCriteriaQuery):
        raw_criteria = query.raw_criteria  # TODO: build criteria from raw
        criteria: Criteria = Criteria()
        await self.__finder.run(criteria)
