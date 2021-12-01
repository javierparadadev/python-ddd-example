from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from tests.contexts.backoffice.users.__mothers__.UserIdMother import UserIdMother
from tests.contexts.backoffice.users.__mothers__.UserNameMother import UserNameMother


class UserMother:

    @staticmethod
    def create(user_id: UserId, name: UserName) -> User:
        return User(user_id, name)

    @staticmethod
    def random() -> User:
        return UserMother.create(UserIdMother.random(), UserNameMother.random())

    @staticmethod
    def with_params(
            user_id: str = None,
            user_name: str = None,
    ) -> User:
        return UserMother.create(
            UserIdMother.with_params(user_id),
            UserNameMother.with_params(user_name),
        )
