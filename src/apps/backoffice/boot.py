import uvicorn
from fastapi import FastAPI, APIRouter

from src.apps.backoffice.routes import register_routes


def boot():
    app: FastAPI = FastAPI()
    router: APIRouter = APIRouter()
    register_routes(router)
    app.include_router(router, prefix='/api/backoffice')
    uvicorn.run(app, host="0.0.0.0", port=8000)
