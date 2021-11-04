from typing import Dict, Optional

from pymongo import MongoClient

from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoConfiguration import PyMongoConfiguration


class PyMongoClientFactory:

    __clients: Dict[str, MongoClient] = {}

    @staticmethod
    def __get_client(context_name: str):
        return PyMongoClientFactory.__clients.get(context_name)

    @staticmethod
    def __add_client(context_name: str, client: MongoClient):
        PyMongoClientFactory.__clients[context_name] = client

    @staticmethod
    def create_instance(context_name: str, config: Optional[PyMongoConfiguration] = None):
        client = PyMongoClientFactory.__get_client(context_name)
        if client is not None:
            return client

        if config is None:
            config = PyMongoConfiguration()
        client = config.create_client_from_config()
        PyMongoClientFactory.__add_client(context_name, client)
        return client
