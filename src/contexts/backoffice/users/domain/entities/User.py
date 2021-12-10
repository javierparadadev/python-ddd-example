from typing import Optional, Dict, List, Union, Any

from src.contexts.backoffice.users.domain.domainevents.UserCreatedDomainEvent import UserCreatedDomainEvent
from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class User(AggregateRoot):

    def __init__(self, user_id: UserId, name: UserName):
        super().__init__()
        self.id = user_id
        self.name = name

    @staticmethod
    def create(user_id: UserId, name: UserName):
        user = User(user_id, name)
        event = UserCreatedDomainEvent(user.id.value(), user)
        user.record_event(event)
        return user

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        user = User(
            UserId(raw_data.get('id')),
            UserName(raw_data.get('name')),
        )
        return user

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
        }
