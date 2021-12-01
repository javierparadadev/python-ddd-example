from src.contexts.backoffice.users.domain.entities.UserId import UserId
from tests.utils.mothers.WordMother import WordMother


class UserIdMother:

    @staticmethod
    def create(user_id: str) -> UserId:
        return UserId(user_id)

    @staticmethod
    def random() -> UserId:
        return UserIdMother.create(WordMother.random())

    @staticmethod
    def with_params(user_id: str = None) -> UserId:
        if user_id is None:
            return UserIdMother.random()
        return UserIdMother.create(user_id)
