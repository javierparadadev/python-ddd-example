from fastapi import APIRouter

from src.apps.backoffice.controllers.StatusGetController import StatusGetController


def register(router: APIRouter):
    status_get_ctr: StatusGetController = StatusGetController()
    router.add_route('/status', status_get_ctr.run)
