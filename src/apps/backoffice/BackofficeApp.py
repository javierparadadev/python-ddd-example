from fastapi import FastAPI, APIRouter

from src.apps.backoffice.routes import register_routes


class BackofficeApp:

    def __init__(self):
        self.__app: FastAPI = FastAPI()
        router: APIRouter = APIRouter()
        register_routes(router)
        self.__app.include_router(router, prefix='/api/backoffice')

    def get_runnable(self):
        return self.__app
