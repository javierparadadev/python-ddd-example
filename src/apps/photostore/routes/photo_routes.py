import sys

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter

from src.apps.photostore.controllers.PhotoPostController import PhotoPostController
from src.apps.photostore.dependencies.PhotoStoreContainer import PhotoStoreContainer, photostore_container


@inject
def register(
        router: APIRouter,
        photo_post_controller: PhotoPostController = Provide[PhotoStoreContainer.photo_post_controller],
):
    router.add_route('/photos', photo_post_controller.run, ['POST'])


photostore_container.wire(modules=[sys.modules[__name__]])
