from pymongo import MongoClient


class PyMongoConfiguration:

    def __init__(
            self,
            host: str = 'localhost',
            port: int = 27017,
    ):
        self.host = host
        self.port = port

    def create_client_from_config(self):
        return MongoClient(
            host=self.host,
            port=self.port,
        )
