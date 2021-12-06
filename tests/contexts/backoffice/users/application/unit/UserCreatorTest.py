import unittest

from src.contexts.backoffice.users.application.createone.UserCreator import UserCreator
from src.contexts.backoffice.users.domain.entities.User import User
from tests.contexts.backoffice.users.__mocks__.EventBusMock import EventBusMock
from tests.contexts.backoffice.users.__mocks__.UserRepositoryMock import UserRepositoryMock
from tests.utils.async_test_decorator import async_test

from tests.contexts.backoffice.users.__mothers__.UserMother import UserMother


class TestUserCreator(unittest.TestCase):

    def setUp(self):
        self.mocked_repo = UserRepositoryMock()
        self.mocked_event_bus = EventBusMock()
        self.user_creator: UserCreator = UserCreator(self.mocked_repo, self.mocked_event_bus)

    @async_test
    async def test_create_user(self):
        """
        Creates user.
        """
        user: User = UserMother.random()
        await self.user_creator.run(user.id, user.name)
        self.mocked_repo.assert_create_one_has_been_called_with(user)


if __name__ == '__main__':
    unittest.main()
