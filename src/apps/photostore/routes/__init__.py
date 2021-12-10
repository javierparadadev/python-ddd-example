from fastapi import APIRouter

from src.apps.photostore.routes.status_routes import register as register_status_routes
from src.apps.photostore.routes.photo_routes import register as register_photo_routes


def register_routes(router: APIRouter):
    register_status_routes(router)
    register_photo_routes(router)
