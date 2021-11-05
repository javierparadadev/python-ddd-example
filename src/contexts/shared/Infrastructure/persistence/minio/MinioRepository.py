from abc import ABC, abstractmethod
from typing import Any

from minio import Minio


class MinioRepository(ABC):

    def __init__(self, client: Minio):
        self.__client = client

    @abstractmethod
    def get_bucket_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_directory_name(self):
        raise NotImplementedError()

    def _create(self, obj_id: str, obj: Any, file_extension: str = None):
        pass
