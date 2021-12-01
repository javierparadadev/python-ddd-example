from typing import NoReturn, List
from unittest.mock import Mock

from src.contexts.backoffice.users.domain.UserRepository import UserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.criteria.Criteria import Criteria
from tests.contexts.backoffice.users.__matchers__.UserMatcher import UserMatcher


class UserRepositoryMock(BaseObject, UserRepository):

    def __init__(self):
        self.__create_one_mock = Mock()

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        raise NotImplementedError()

    # ----------------------------------------------------
    # ------------------ CREATE ONE ----------------------
    # ----------------------------------------------------

    async def create_one(self, user: User) -> NoReturn:
        self.__create_one_mock(user)

    def assert_create_one_has_been_called(self):
        assert self.__create_one_mock.called

    def assert_create_one_has_been_called_with(self, user: User):
        user_matcher = UserMatcher(user)
        self.__create_one_mock.assert_called_with(user_matcher)
