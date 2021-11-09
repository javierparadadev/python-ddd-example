from datetime import datetime
from typing import Any, Optional

from src.contexts.shared.domain.DomainEvent import DomainEvent


class UserCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'user-created'

    def __init__(
            self,
            aggregate_id: str,
            event_id: Optional[str],
            occurred_on: Optional[datetime],
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)

    def to_primitives(self) -> Any:
        return {
            'user-id': self.aggregate_id,
            'event-id': self.id,
            'occurred-on': self.occurred_on,
            'created-at': self.created_at,
        }
