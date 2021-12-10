from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.apps.photostore.controllers.PhotoPostController import PhotoPostController
from src.contexts.photostore.photo.application.createone.CreatePhotoCommandHandler import CreatePhotoCommandHandler
from src.contexts.photostore.photo.application.createone.PhotoCreator import PhotoCreator
from src.contexts.photostore.photo.infrastructure.persistence.MinioPhotoStorePhotoRepository import MinioPhotoRepository
from src.contexts.photostore.photo.infrastructure.persistence.config.MinioPhotoConfigFactory import \
    MinioPhotoConfigFactory
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.minio.MinioClientFactory import MinioClientFactory


class PhotoStoreContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(MinioPhotoConfigFactory.create)
    db_client = providers.Singleton(MinioClientFactory.create_instance, 'photostore', db_config)

    photo_repository = providers.Singleton(MinioPhotoRepository, db_client)

    photo_creator = providers.Singleton(PhotoCreator, photo_repository, event_bus)
    create_photo_command_handler = providers.Singleton(
        CreatePhotoCommandHandler,
        photo_creator,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_photo_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    photo_post_controller = providers.Singleton(PhotoPostController, command_bus)


photostore_container: PhotoStoreContainer = PhotoStoreContainer()


