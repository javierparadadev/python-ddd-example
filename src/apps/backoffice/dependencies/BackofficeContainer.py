from dependency_injector import containers, providers

from src.apps.backoffice.controllers.StatusGetController import StatusGetController


class BackofficeContainer(containers.DeclarativeContainer):

    status_get_controller = providers.Singleton(StatusGetController)


backoffice_container: BackofficeContainer = BackofficeContainer()


