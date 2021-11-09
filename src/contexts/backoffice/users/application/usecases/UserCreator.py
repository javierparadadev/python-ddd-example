from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.domain.EventBus import EventBus


class UserCreator:

    def __init__(self, user_repository: BackofficeUserRepository, event_bus: EventBus):
        self.__user_repository = user_repository
        self.__event_bus = event_bus

    async def run(self, user: User):
        await self.__user_repository.create_one(user)
