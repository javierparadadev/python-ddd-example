import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.photostore.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        status_get_controller: StatusGetController = Provide[BackofficeContainer.status_get_controller]
):
    router.add_route('/status', status_get_controller.run)


backoffice_container.wire(modules=[sys.modules[__name__]])
