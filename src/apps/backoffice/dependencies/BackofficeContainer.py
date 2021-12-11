from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.controllers.UsersGetController import UsersGetController
from src.apps.backoffice.controllers.UserPostController import UserPostController
from src.contexts.backoffice.users.application.createone.CreateUserCommandHandler import CreateUserCommandHandler
from src.contexts.backoffice.users.application.findall.FindUsersByCriteriaQueryHandler import \
    FindUsersByCriteriaQueryHandler
from src.contexts.backoffice.users.application.createone.UserCreator import UserCreator
from src.contexts.backoffice.users.application.findall.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.backoffice.users.infrastructure.persistence.PyMongoUserRepository import \
    PyMongoUserRepository
from src.contexts.backoffice.users.infrastructure.persistence.config.PyMongoUserConfigFactory import PyMongoUserConfigFactory
from src.contexts.shared.Infrastructure.commandbus.InMemoryCommandBus import InMemoryCommandBus
from src.contexts.shared.Infrastructure.eventbus.InMemoryEventBus import InMemoryEventBus
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class BackofficeContainer(containers.DeclarativeContainer):

    event_bus = providers.Singleton(
        InMemoryEventBus,
    )

    db_config = providers.Singleton(PyMongoUserConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'backoffice', db_config)

    user_repository = providers.Singleton(PyMongoUserRepository, db_client)

    users_by_criteria_finder = providers.Singleton(UsersByCriteriaFinder, user_repository)
    find_users_by_criteria_query_handler = providers.Singleton(
        FindUsersByCriteriaQueryHandler,
        users_by_criteria_finder,
    )

    user_creator = providers.Singleton(UserCreator, user_repository, event_bus)
    create_user_command_handler = providers.Singleton(
        CreateUserCommandHandler,
        user_creator,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_users_by_criteria_query_handler,
    )

    command_bus = providers.Singleton(
        InMemoryCommandBus,
        create_user_command_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    users_get_controller = providers.Singleton(UsersGetController, query_bus)
    user_post_controller = providers.Singleton(UserPostController, command_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


