from typing import NoReturn, List
from unittest.mock import MagicMock

from src.contexts.backoffice.users.domain.UserRepository import UserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.criteria.Criteria import Criteria


class UserRepositoryMock(BaseObject, UserRepository):

    def __init__(self):
        self.__create_one_mock = MagicMock()

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        raise NotImplementedError()

    async def create_one(self, _: User) -> NoReturn:
        self.__create_one_mock()

    def assert_create_one_has_been_called(self):
        assert self.__create_one_mock.called
