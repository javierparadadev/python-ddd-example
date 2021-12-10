import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.backoffice.controllers.UsersGetController import UsersGetController
from src.apps.backoffice.controllers.UserPostController import UserPostController
from src.apps.backoffice.dependencies.BackofficeContainer import BackofficeContainer, backoffice_container


@inject
def register(
        router: APIRouter,
        users_get_controller: UsersGetController = Provide[BackofficeContainer.users_get_controller],
        user_post_controller: UserPostController = Provide[BackofficeContainer.user_post_controller],
):
    router.add_route('/users', users_get_controller.run)
    router.add_route('/users', user_post_controller.run, ['POST'])


backoffice_container.wire(modules=[sys.modules[__name__]])
