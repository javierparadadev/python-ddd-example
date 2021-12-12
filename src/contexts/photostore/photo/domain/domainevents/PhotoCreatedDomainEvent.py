from datetime import datetime
from typing import Any, Optional

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.photostore.photo.domain.entities.Photo import Photo
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class PhotoCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'photostore.photo.created'

    def __init__(
            self,
            aggregate_id: str,
            photo_id: PhotoId,
            user_id: UserId,
            photo_name: PhotoName,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)
        self.photo_id = photo_id
        self.user_id = user_id
        self.photo_name = photo_name

    def to_primitives(self) -> Any:
        return {
            'data': {
                'id': self.id,
                'aggregate-id': self.aggregate_id,
                'occurred-on': self.occurred_on,
                'created-at': self.created_at,
                'type': PhotoCreatedDomainEvent.EVENT_TYPE,
                'attributes': {
                    'id': self.photo_id.value(),
                    'user-id': self.user_id.value(),
                    'name': self.photo_name.value(),
                }
            },
            'meta': {
                'attempts': 0,
            }
        }

