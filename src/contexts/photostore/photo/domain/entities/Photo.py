from typing import Dict, List, Union, Any

from src.contexts.photostore.photo.domain.domainevents.PhotoCreatedDomainEvent import PhotoCreatedDomainEvent
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photo.domain.entities.UserId import UserId
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Photo(AggregateRoot):

    def __init__(self, photo_id: PhotoId, name: PhotoName, user_id: UserId):
        super().__init__()
        self.id = photo_id
        self.name = name
        self.user_id = user_id

    @staticmethod
    def create(photo_id: PhotoId, name: PhotoName, user_id: UserId):
        photo = Photo(photo_id, name, user_id)
        event = PhotoCreatedDomainEvent(photo.id.value(), photo)
        photo.record_event(event)
        return photo

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        photo = Photo(
            PhotoId(raw_data.get('id')),
            PhotoName(raw_data.get('name')),
            UserId(raw_data.get('user-id')),
        )
        return photo

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
        }
