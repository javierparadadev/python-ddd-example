from datetime import datetime
from typing import Any, Optional, Dict

from deepfinder import deep_find

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photo.domain.entities.PhotoTag import PhotoTag
from src.contexts.photostore.photo.domain.entities.PhotoTags import PhotoTags
from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class PhotoRegistryCreatedDomainEvent(DomainEvent):

    EVENT_TYPE = 'photostore.photoregistry.created'

    def __init__(
            self,
            aggregate_id: str,
            photo_id: PhotoId,
            user_id: UserId,
            photo_name: PhotoName,
            tags: PhotoTags,
            event_id: Optional[str] = None,
            occurred_on: Optional[datetime] = None,
    ):
        super().__init__(self.EVENT_TYPE, aggregate_id, event_id, occurred_on)
        self.photo_id = photo_id
        self.user_id = user_id
        self.photo_name = photo_name
        self.tags = tags

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        photo = PhotoRegistryCreatedDomainEvent(
            deep_find(raw_data, 'data.aggregate-id'),
            PhotoId(deep_find(raw_data, 'data.attributes.id')),
            UserId(deep_find(raw_data, 'data.attributes.user-id')),
            PhotoName(deep_find(raw_data, 'data.attributes.name')),
            PhotoTags([PhotoTag(tag) for tag in deep_find(raw_data, 'data.attributes.tags')]),
            event_id=deep_find(raw_data, 'data.id'),
            occurred_on=deep_find(raw_data, 'data.occurred-on'),
        )
        return photo

    def to_primitives(self) -> Dict[Any, Any]:
        return {
            'data': {
                'id': self.id,
                'aggregate-id': self.aggregate_id,
                'occurred-on': self.occurred_on,
                'created-at': self.created_at,
                'type': PhotoRegistryCreatedDomainEvent.EVENT_TYPE,
                'attributes': {
                    'id': self.photo_id.value(),
                    'user-id': self.user_id.value(),
                    'name': self.photo_name.value(),
                    'tags': self.tags.values(),
                },
            },
            'meta': {
                'attempts': 0,
            }
        }

