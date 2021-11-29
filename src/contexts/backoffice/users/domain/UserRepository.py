from abc import ABC
from typing import List, NoReturn

from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.criteria.Criteria import Criteria


class UserRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        raise NotImplementedError()

    async def create_one(self, user: User) -> NoReturn:
        raise NotImplementedError()
