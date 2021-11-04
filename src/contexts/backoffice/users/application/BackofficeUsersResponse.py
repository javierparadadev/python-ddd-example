from typing import List, Any

from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.application.Response import Response


class BackofficeUsersResponse(Response):

    def __init__(self, users: List[User]):
        self.__users = users

    def to_primitives(self) -> Any:
        json_users = [user.to_primitives() for user in self.__users]
        return json_users
