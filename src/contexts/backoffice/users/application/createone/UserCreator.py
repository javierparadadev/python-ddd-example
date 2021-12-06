from src.contexts.backoffice.users.domain.UserRepository import UserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.EventBus import EventBus


class UserCreator:

    def __init__(self, user_repository: UserRepository, event_bus: EventBus):
        self.__user_repository = user_repository
        self.__event_bus = event_bus

    async def run(self, user_id: UserId, name: UserName):
        user: User = User.create(user_id, name)
        await self.__user_repository.create_one(user)
        await self.__event_bus.publish(user.pull_domain_events())
