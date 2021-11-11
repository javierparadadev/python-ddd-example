import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.backoffice.controllers.StatusGetController import StatusGetController
from src.apps.backoffice.controllers.UsersGetController import UsersGetController
from src.apps.backoffice.controllers.UsersPostController import UsersPostController
from src.apps.backoffice.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        users_get_controller: UsersGetController = Provide[BackofficeContainer.users_get_controller],
        users_post_controller: UsersPostController = Provide[BackofficeContainer.users_post_controller],
):
    router.add_route('/users', users_get_controller.run)
    router.add_route('/users', users_post_controller.run, ['POST'])


backoffice_container.wire(modules=[sys.modules[__name__]])
