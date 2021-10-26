from fastapi import Request
from fastapi.responses import JSONResponse


class BackofficeController:

    def run(self, req: Request) -> JSONResponse:
        raise NotImplementedError()
