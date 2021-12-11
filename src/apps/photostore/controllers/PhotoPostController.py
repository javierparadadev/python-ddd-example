from typing import Dict, Any

from fastapi import File, Form, Body, UploadFile
from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.users.application.createone.CreateUserCommand import CreatePhotoCommand
from src.contexts.backoffice.users.infrastructure.JsonResponseErrorHandler import JsonResponseErrorHandler
from src.contexts.shared.domain.CommandBus import CommandBus
from src.contexts.shared.domain.errors.DomainError import DomainError
from src.utils.BytifyUploadFile import bytify_upload_file


class PhotoPostController(BackofficeController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self.__command_bus = command_bus
        self.__error_handler = JsonResponseErrorHandler()

    async def run(
            self,
            request: Request,
    ) -> JSONResponse:
        form = await request.form()
        body = dict(form)
        file: UploadFile = body.get('file')
        raw_data = await bytify_upload_file(file)
        command: CreatePhotoCommand = CreatePhotoCommand(body['id'], body['name'], body['user-id'], raw_data)
        try:
            await self.__command_bus.dispatch(command)
        except DomainError as err:
            return self.__error_handler.resolve(err)

        return JSONResponse(status_code=HTTPStatus.CREATED)
