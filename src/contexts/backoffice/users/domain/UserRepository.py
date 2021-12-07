from abc import ABC
from typing import List, NoReturn, Tuple, Optional

from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class UserRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[User], Optional[CriteriaQueryMetadata]]:
        raise NotImplementedError()

    async def create_one(self, user: User) -> NoReturn:
        raise NotImplementedError()
