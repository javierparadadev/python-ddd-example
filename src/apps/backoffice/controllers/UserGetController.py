from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.users.application.queries.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.shared.application.Response import Response
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus


class UserGetController(BackofficeController):

    def __init__(
            self,
            query_bus: QueryBus,
    ):
        self.__query_bus = query_bus

    async def run(self, req: Request) -> JSONResponse:
        query: Query = FindUsersByCriteriaQuery(dict(req.query_params))
        res: Response = await self.__query_bus.ask(query)
        return JSONResponse(status_code=HTTPStatus.OK, content=res.to_json())
