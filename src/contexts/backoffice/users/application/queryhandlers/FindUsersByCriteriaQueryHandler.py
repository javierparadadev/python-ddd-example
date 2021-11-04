from src.contexts.backoffice.users.application.queries.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.backoffice.users.application.usecases.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindUsersByCriteriaQueryHandler:

    __subscription: str = FindUsersByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: UsersByCriteriaFinder):
        self.__finder = finder

    def subscribed_to(self) -> object:
        return self.__subscription

    async def handle(self, query: FindUsersByCriteriaQuery):
        raw_criteria = query.raw_criteria  # TODO: build criteria from raw
        criteria: Criteria = Criteria()
        await self.__finder.run(criteria)
