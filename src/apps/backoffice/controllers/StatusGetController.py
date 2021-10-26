from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.shared.AppObject import AppObject


class StatusGetController(AppObject, BackofficeController):

    def run(self, req: Request) -> JSONResponse:
        return JSONResponse(status_code=HTTPStatus.OK)
