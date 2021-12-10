from datetime import datetime
from typing import Any, Optional

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class UserCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'backoffice.user.created'

    def __init__(
            self,
            aggregate_id: str,
            entity: AggregateRoot,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)
        self.entity = entity

    def to_primitives(self) -> Any:
        return {
            'data': {
                'id': self.id,
                'aggregate-id': self.aggregate_id,
                'occurred-on': self.occurred_on,
                'created-at': self.created_at,
                'type': UserCreatedDomainEvent.EVENT_TYPE,
                'attributes': self.entity.to_primitives(),
            },
            'meta': {
                'attempts': 0,
            }
        }
