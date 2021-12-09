from typing import Dict, Optional

from minio import Minio

from src.contexts.shared.Infrastructure.persistence.minio.MinioConfiguration import MinioConfiguration
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoConfiguration import PyMongoConfiguration


class MinioClientFactory:

    __clients: Dict[str, Minio] = {}

    @staticmethod
    def __get_client(context_name: str):
        return MinioClientFactory.__clients.get(context_name)

    @staticmethod
    def __add_client(context_name: str, client: Minio):
        MinioClientFactory.__clients[context_name] = client

    @staticmethod
    def create_instance(context_name: str, config: Optional[PyMongoConfiguration] = None):
        client = MinioClientFactory.__get_client(context_name)
        if client is not None:
            return client

        if config is None:
            config = MinioConfiguration()
        client = config.create_client_from_config()
        MinioClientFactory.__add_client(context_name, client)
        return client
