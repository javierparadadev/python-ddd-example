from typing import NoReturn, List

from src.contexts.backoffice.users.domain.UserRepository import UserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.criteria.Criteria import Criteria


class UserRepositoryMock(BaseObject, UserRepository):

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        raise NotImplementedError()

    async def create_one(self, user: User) -> NoReturn:
        pass