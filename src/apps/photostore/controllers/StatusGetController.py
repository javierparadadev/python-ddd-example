from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.photostore.controllers.PhotoStoreController import PhotoStoreController


class StatusGetController(PhotoStoreController):

    def __init__(self):
        pass

    async def run(self, req: Request) -> JSONResponse:
        return JSONResponse(status_code=HTTPStatus.OK)
