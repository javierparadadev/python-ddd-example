import uvicorn

from src.apps.photostore.PtohoStoreApp import PhotoStoreApp
from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar


class PhotoStoreServer:

    def __init__(self):
        self.app = PhotoStoreApp()

    def run(self):
        host = EnvManager.get(EnvVar.PHOTOSTORE_SERVER_HOST)
        port = EnvManager.get(EnvVar.PHOTOSTORE_SERVER_PORT, parser=int)
        uvicorn.run(self.app.get_runnable(), host=host, port=port)
