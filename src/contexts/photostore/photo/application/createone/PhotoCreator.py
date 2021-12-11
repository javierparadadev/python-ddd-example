from src.contexts.photostore.photo.domain.PhotoRepository import PhotoRepository
from src.contexts.photostore.photo.domain.entities.Photo import Photo
from src.contexts.photostore.photo.domain.entities.PhotoFile import PhotoFile
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photo.domain.entities.UserId import UserId
from src.contexts.shared.domain.EventBus import EventBus


class PhotoCreator:

    def __init__(self, photo_repository: PhotoRepository, event_bus: EventBus):
        self.__photo_repository = photo_repository
        self.__event_bus = event_bus

    async def run(self, photo_id: PhotoId, name: PhotoName, user_id: UserId, file: PhotoFile):
        photo: Photo = Photo.create(photo_id, name, user_id, file)
        await self.__photo_repository.create_one(photo)
        await self.__event_bus.publish(photo.pull_domain_events())
