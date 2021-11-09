from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.controllers.UsersGetController import UsersGetController
from src.contexts.backoffice.users.application.queries.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.backoffice.users.application.queryhandlers.FindUsersByCriteriaQueryHandler import \
    FindUsersByCriteriaQueryHandler
from src.contexts.backoffice.users.application.usecases.UsersByCriteriaFinder import UsersByCriteriaFinder
from src.contexts.backoffice.users.infrastructure.persistence.PyMongoBackofficeUserRepository import \
    PyMongoBackofficeUserRepository
from src.contexts.backoffice.users.infrastructure.persistence.config.PyMongoUserConfigFactory import PyMongoUserConfigFactory
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoClientFactory import PyMongoClientFactory
from src.contexts.shared.Infrastructure.querybus.InMemoryQueryBus import InMemoryQueryBus


class BackofficeContainer(containers.DeclarativeContainer):

    db_config = providers.Singleton(PyMongoUserConfigFactory.create)
    db_client = providers.Singleton(PyMongoClientFactory.create_instance, 'backoffice', db_config)

    user_repository = providers.Singleton(PyMongoBackofficeUserRepository, db_client)
    users_by_criteria_finder = providers.Singleton(UsersByCriteriaFinder, user_repository)
    find_users_by_criteria_query_handler = providers.Singleton(
        FindUsersByCriteriaQueryHandler,
        users_by_criteria_finder,
    )

    query_bus = providers.Singleton(
        InMemoryQueryBus,
        find_users_by_criteria_query_handler,
    )

    status_get_controller = providers.Singleton(StatusGetController)
    users_get_controller = providers.Singleton(UsersGetController, query_bus)


backoffice_container: BackofficeContainer = BackofficeContainer()


