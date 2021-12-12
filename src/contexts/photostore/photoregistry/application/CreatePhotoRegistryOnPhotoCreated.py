from typing import List

from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.photostore.photo.domain.domainevents.PhotoCreatedDomainEvent import PhotoCreatedDomainEvent
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photoregistry.application.PhotoRegistryCreator import PhotoRegistryCreator
from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.EventSubscriber import EventSubscriber


class CreatePhotoRegistryOnPhotoCreated(BaseObject, EventSubscriber):

    __SUBSCRIPTIONS = [PhotoCreatedDomainEvent.EVENT_TYPE]

    def __init__(self, creator: PhotoRegistryCreator):
        self.__creator = creator

    def subscribed_to(self) -> List[str]:
        return CreatePhotoRegistryOnPhotoCreated.__SUBSCRIPTIONS

    async def on(self, event: PhotoCreatedDomainEvent):
        photo_id: PhotoId = event.photo_id
        photo_name: PhotoName = event.photo_name
        user_id: UserId = event.user_id
        await self.__creator.run(photo_id, photo_name, user_id)
