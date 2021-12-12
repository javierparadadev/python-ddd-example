from src.contexts.backoffice.users.domain.entities.UserId import UserId
from src.contexts.photostore.photo.domain.entities.PhotoId import PhotoId
from src.contexts.photostore.photo.domain.entities.PhotoName import PhotoName
from src.contexts.photostore.photoregistry.domain.PhotoRegistryRepository import PhotoRegistryRepository
from src.contexts.photostore.photoregistry.domain.entities.PhotoRegistry import PhotoRegistry
from src.contexts.shared.domain.EventBus import EventBus


class PhotoRegistryCreator:

    def __init__(self, photo_registry_repository: PhotoRegistryRepository, event_bus: EventBus):
        self.__photo_repository = photo_registry_repository
        self.__event_bus = event_bus

    async def run(self, photo_id: PhotoId, name: PhotoName, user_id: UserId):
        photo_registry: PhotoRegistry = PhotoRegistry.create(photo_id, name, user_id)
        await self.__photo_repository.create_one(photo_registry)
        await self.__event_bus.publish(photo_registry.pull_domain_events())
