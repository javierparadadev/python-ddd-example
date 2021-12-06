from typing import Optional, Dict, List, Union, Any

from src.contexts.photostore.photo.domain.domainevents.PhotoCreatedDomainEvent import PhotoCreatedDomainEvent
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.shared.domain.valueobj.AggregateRoot import AggregateRoot


class Photo(AggregateRoot):

    def __init__(self, photo_id: PhotoId, name: PhotoName):
        super().__init__()
        self.id = photo_id
        self.name = name

    @staticmethod
    def create(user_id: PhotoId, name: PhotoName):
        user = Photo(user_id, name)
        event = PhotoCreatedDomainEvent(user.id.value())
        user.record_event(event)
        return user

    @staticmethod
    def create_from_primitives(raw_data: Dict[str, Any]):
        user = Photo(
            PhotoId(raw_data.get('id')),
            PhotoName(raw_data.get('name')),
        )
        return user

    def to_primitives(self) -> Union[Dict, List]:
        return {
            'id': self.id.value(),
            'name': self.name.value(),
        }
