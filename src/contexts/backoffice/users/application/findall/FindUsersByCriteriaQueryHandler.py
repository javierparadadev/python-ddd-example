from src.contexts.backoffice.users.application.BackofficeUsersResponse import BackofficeUsersResponse
from src.contexts.backoffice.users.application.findall.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.backoffice.users.application.findall.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.shared.domain.QueryHandler import QueryHandler
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindUsersByCriteriaQueryHandler(QueryHandler):

    __subscription: str = FindUsersByCriteriaQuery.QUERY_TYPE

    def __init__(self, finder: UsersByCriteriaFinder):
        self.__finder = finder

    def subscribed_to(self) -> str:
        return self.__subscription

    async def handle(self, query: FindUsersByCriteriaQuery) -> BackofficeUsersResponse:
        criteria = Criteria(query.filters, query.order_by, query.limit)
        return await self.__finder.run(criteria)
