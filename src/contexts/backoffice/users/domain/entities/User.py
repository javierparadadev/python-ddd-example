from typing import Optional, Dict, List

from src.contexts.backoffice.users.domain.entities.UserEmail import UserEmail
from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.backoffice.users.domain.entities.UserName import UserName
from src.contexts.shared.domain.value_obj.AggregateRoot import AggregateRoot


class User(AggregateRoot):

    def __init__(self, id: UserId, email: UserEmail, name: UserName):
        self.id = id
        self.email = email
        self.name = name

    def to_primitives(self) -> Optional[Dict, List]:
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
        }
