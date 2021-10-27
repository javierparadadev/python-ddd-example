from abc import ABC
from typing import List

from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.criteria.Criteria import Criteria


class BackofficeUserRepository(ABC):

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        raise NotImplementedError()
