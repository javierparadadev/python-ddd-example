from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus

from src.apps.backoffice.controllers.BackofficeController import BackofficeController
from src.contexts.backoffice.users.application.queries.FindUsersByCriteriaQuery import FindUsersByCriteriaQuery
from src.contexts.shared.Infrastructure.parsers.parse_dict_format_to_criteria import parse_dict_to_criteria
from src.contexts.shared.application.Response import Response
from src.contexts.shared.domain.Query import Query
from src.contexts.shared.domain.QueryBus import QueryBus


class UsersGetController(BackofficeController):

    def __init__(
            self,
            query_bus: QueryBus,
    ):
        self.__query_bus = query_bus

    async def run(self, req: Request) -> JSONResponse:
        query_params = dict(req.query_params)
        filters, order_by, _ = parse_dict_to_criteria(query_params)
        query: Query = FindUsersByCriteriaQuery(filters, order_by)
        res: Response = await self.__query_bus.ask(query)
        return JSONResponse(status_code=HTTPStatus.OK, content=res.to_primitives())
