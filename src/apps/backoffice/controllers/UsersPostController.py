from typing import Dict, Any

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.users.application.commands.CreateUserCommand import CreateUserCommand
from src.contexts.shared.domain.CommandBus import CommandBus


class UsersPostController(BackofficeController):

    def __init__(
            self,
            command_bus: CommandBus,
    ):
        self.__command_bus = command_bus

    async def run(self, req: Request) -> JSONResponse:
        body: Dict[str, Any] = await req.json()
        command: CreateUserCommand = CreateUserCommand(body['id'], body['name'])
        await self.__command_bus.dispatch(command)
        return JSONResponse(status_code=HTTPStatus.CREATED)
