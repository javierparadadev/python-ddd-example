from fastapi import APIRouter

from src.apps.backoffice.routes.status_routes import register


def register_routes(router: APIRouter):
    register(router)
