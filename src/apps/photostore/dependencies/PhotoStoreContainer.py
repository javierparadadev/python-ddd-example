from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.apps.photostore.controllers.PhotoPostController import PhotoPostController
from src.contexts.photostore.photo.application.createone.CreatePhotoCommandHandler import CreatePhotoCommandHandler
from src.contexts.photostore.photo.application.createone.PhotoCreator import PhotoCreator
from src.contexts.photostore.photo.infrastructure.persistence.MinioPhotoStorePhotoRepository import MinioPhotoRepository
from src.contexts.photostore.photo.infrastructure.persistence.config.MinioPhotoConfigFactory import \
    MinioPhotoConfigFactory
from src.contexts.photostore.photoregistry.application.CreatePhotoRegistryOnPhotoCreated import \
    CreatePhotoRegistryOnPhotoCreated
from src.contexts.photostore.photoregistry.application.PhotoRegistryCreator import PhotoRegistryCreator
from src.contexts.photostore.photoregistry.infrastructure.persistence.PyMongoPhotoRegistryRepository import \
    PyMongoPhotoRegistryRepository
from src.contexts.photostore.photoregistry.infrastructure.persistence.config.PyMongoPhotoRegistryConfigFactory import \
    PyMongoPhotoRegistryConfigFactory
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.minio.MinioClientFactory import MinioClientFactory
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory


class PhotoStoreContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    photo_minio_config = providers.Singleton(MinioPhotoConfigFactory.create)
    photo_minio_client = providers.Singleton(MinioClientFactory.create_instance, 'photo', photo_minio_config)

    photo_registry_mongo_config = providers.Singleton(PyMongoPhotoRegistryConfigFactory.create)
    photo_registry_mongo_client = providers.Singleton(PyMongoClientFactory.create_instance, 'photo-registry',
                                                      photo_registry_mongo_config)

    photo_repository = providers.Singleton(MinioPhotoRepository, photo_minio_client)
    photo_registry_repository = providers.Singleton(PyMongoPhotoRegistryRepository, photo_registry_mongo_client)

    photo_creator = providers.Singleton(PhotoCreator, photo_repository, event_bus)
    photo_registry_creator = providers.Singleton(PhotoRegistryCreator, photo_registry_repository, event_bus)

    create_photo_command_handler = providers.Singleton(
        CreatePhotoCommandHandler,
        photo_creator,
    )
    create_photo_registry_on_photo_created = providers.Singleton(
        CreatePhotoRegistryOnPhotoCreated,
        photo_registry_creator,
        event_bus,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_photo_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    photo_post_controller = providers.Singleton(PhotoPostController, command_bus)


photostore_container: PhotoStoreContainer = PhotoStoreContainer()

photostore_container.create_photo_registry_on_photo_created.reset()
photostore_container.create_photo_registry_on_photo_created()


