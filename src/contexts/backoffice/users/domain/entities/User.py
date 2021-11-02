from typing import Optional, Dict, List

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class User(AggregateRoot):

    def __init__(self, id: UserId, name: UserName):
        self.id = id
        self.name = name

    def to_primitives(self) -> Optional[Dict, List]:
        return {
            'id': self.id,
            'name': self.name,
        }
