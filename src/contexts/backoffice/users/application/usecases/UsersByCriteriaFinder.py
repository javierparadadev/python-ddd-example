from src.contexts.backoffice.users.application.BackofficeUsersResponse import BackofficeUsersResponse
from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class UsersByCriteriaFinder:

    def __init__(self, user_repository: BackofficeUserRepository):
        self.__user_repository = user_repository

    async def run(self, criteria: Criteria) -> BackofficeUsersResponse:
        users = await self.__user_repository.find_by_criteria(criteria)
        return BackofficeUsersResponse(users)

