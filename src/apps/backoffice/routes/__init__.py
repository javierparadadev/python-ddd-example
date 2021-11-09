from fastapi import APIRouter

from src.apps.backoffice.routes.status_routes import register as register_status_routes
from src.apps.backoffice.routes.user_routes import register as register_user_routes


def register_routes(router: APIRouter):
    register_status_routes(router)
    register_user_routes(router)
