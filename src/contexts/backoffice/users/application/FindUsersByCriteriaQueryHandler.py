from src.contexts.backoffice.users.application.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.backoffice.users.application.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.shared.domain.criteria.Criteria import Criteria


class FindUsersByCriteriaQueryHandler:

    __subscription = FindUsersByCriteriaQuery

    def __init__(self, finder: UsersByCriteriaFinder):
        self.__finder = finder

    def subscribed_to(self) -> object:
        return self.__subscription

    async def handle(self, query: FindUsersByCriteriaQuery):
        criteria: Criteria = Criteria()
        await self.__finder.run(criteria)
