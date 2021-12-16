from typing import Dict, List, Union, Any

from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photo.domain.entities.PhotoTag import PhotoTag
from src.contexts.photostore.photo.domain.entities.PhotoTags import PhotoTags
from src.contexts.photostore.photo.domain.entities.UserId import UserId
from src.contexts.photostore.photoregistry.domain.domainevents.PhotoRegistryCreatedDomainEvent import \
    PhotoRegistryCreatedDomainEvent
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class PhotoRegistry(AggregateRoot):

    def __init__(self, photo_id: PhotoId, name: PhotoName, user_id: UserId, tags: PhotoTags):
        super().__init__()
        self.id = photo_id
        self.name = name
        self.user_id = user_id
        self.tags = tags

    @staticmethod
    def create(photo_id: PhotoId, name: PhotoName, user_id: UserId, tags: PhotoTags):
        photo_registry = PhotoRegistry(photo_id, name, user_id, tags)
        event = PhotoRegistryCreatedDomainEvent(photo_registry.id.value(), photo_registry, tags)
        photo_registry.record_event(event)
        return photo_registry

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        photo_registry = PhotoRegistry(
            PhotoId(raw_data.get('id')),
            PhotoName(raw_data.get('name')),
            UserId(raw_data.get('user-id')),
            PhotoTags([PhotoTag(tag) for tag in raw_data.get('tags', default=[])]),
        )
        return photo_registry

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
            'user-id': self.user_id.value(),
            'tags': self.tags.values(),
        }
