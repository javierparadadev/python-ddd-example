from typing import Dict, List, Union, Any

from src.contexts.photostore.photo.domain.domainevents.PhotoCreatedDomainEvent import PhotoCreatedDomainEvent
from src.contexts.photostore.photo.domain.entities.PhotoFile import PhotoFile
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photo.domain.entities.PhotoTag import PhotoTag
from src.contexts.photostore.photo.domain.entities.PhotoTags import PhotoTags
from src.contexts.photostore.photo.domain.entities.UserId import UserId
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Photo(AggregateRoot):

    def __init__(
            self,
            photo_id: PhotoId,
            name: PhotoName,
            user_id: UserId,
            file: PhotoFile,
            tags: PhotoTags,
    ):
        super().__init__()
        self.id = photo_id
        self.name = name
        self.user_id = user_id
        self.file = file
        self.tags = tags

    @staticmethod
    def create(photo_id: PhotoId, name: PhotoName, user_id: UserId, file: PhotoFile, tags: PhotoTags):
        photo = Photo(photo_id, name, user_id, file, tags)
        event = PhotoCreatedDomainEvent(photo.id.value(), photo_id, user_id, name, tags)
        photo.record_event(event)
        return photo

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        photo = Photo(
            PhotoId(raw_data.get('id')),
            PhotoName(raw_data.get('name')),
            UserId(raw_data.get('user-id')),
            PhotoFile(raw_data.get('file')),
            PhotoTags([PhotoTag(tag) for tag in raw_data.get('tags', default=[])]),
        )
        return photo

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
            'user-id': self.user_id.value(),
            'tags': self.tags.values(),
        }
