from fastapi import FastAPI, APIRouter

from src.apps.photostore.routes import register_routes


class PhotoStoreApp:

    def __init__(self):
        self.__app: FastAPI = FastAPI()
        router: APIRouter = APIRouter()
        register_routes(router)
        self.__app.include_router(router, prefix='/api')

    def get_runnable(self):
        return self.__app
