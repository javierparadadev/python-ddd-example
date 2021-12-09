from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.contexts.backoffice.users.application.createone.CreateUserCommandHandler import CreateUserCommandHandler
from src.contexts.backoffice.users.application.createone.UserCreator import UserCreator
from src.contexts.photostore.photo.infrastructure.persistence.MinioPhotoStorePhotoRepository import MinioPhotoRepository
from src.contexts.photostore.photo.infrastructure.persistence.config.MinioPhotoConfigFactory import \
    MinioPhotoConfigFactory
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.minio.MinioClientFactory import MinioClientFactory


class PhotoStoreContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(MinioPhotoConfigFactory.create)
    db_client = providers.Singleton(MinioClientFactory.create_instance, 'photostore', db_config)

    user_repository = providers.Singleton(MinioPhotoRepository, db_client)

    user_creator = providers.Singleton(UserCreator, user_repository, event_bus)
    create_user_command_handler = providers.Singleton(
        CreateUserCommandHandler,
        user_creator,
    )

    status_get_controller = providers.Singleton(StatusGetController)


backoffice_container: PhotoStoreContainer = PhotoStoreContainer()


