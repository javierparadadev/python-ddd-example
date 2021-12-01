from src.contexts.backoffice.users.domain.entities.UserName import UserName
from tests.utils.mothers.WordMother import WordMother


class UserNameMother:

    @staticmethod
    def create(user_name: str) -> UserName:
        return UserName(user_name)

    @staticmethod
    def random() -> UserName:
        return UserNameMother.create(WordMother.random())

    @staticmethod
    def with_params(user_name: str = None) -> UserName:
        if user_name is None:
            return UserNameMother.random()
        return UserNameMother.create(user_name)
