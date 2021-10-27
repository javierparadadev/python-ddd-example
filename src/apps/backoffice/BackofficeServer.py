import uvicorn

from src.apps.backoffice.BackofficeApp import BackofficeApp


class BackofficeServer:

    def __init__(self):
        self.app = BackofficeApp()

    def run(self):
        uvicorn.run(self.app.get_runnable(), host="0.0.0.0", port=8000)
