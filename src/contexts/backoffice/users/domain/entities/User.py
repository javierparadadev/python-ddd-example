from typing import Optional, Dict, List, Union

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class User(AggregateRoot):

    def __init__(self, user_id: UserId, name: UserName):
        super().__init__()
        self.id = user_id
        self.name = name

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id,
            'name': self.name,
        }
