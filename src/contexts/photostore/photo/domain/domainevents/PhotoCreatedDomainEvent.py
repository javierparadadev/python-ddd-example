from datetime import datetime
from typing import Any, Optional

from src.contexts.shared.domain.DomainEvent import DomainEvent


class PhotoCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'photostore-photo-created'

    def __init__(
            self,
            aggregate_id: str,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)

    def to_primitives(self) -> Any:
        return {
            'aggregate-id': self.aggregate_id,
            'id': self.id,
            'occurred-on': self.occurred_on,
            'created-at': self.created_at,
            'type': PhotoCreatedDomainEvent.EVENT_TYPE,
        }
