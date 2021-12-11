import io
import json
from abc import ABC, abstractmethod
from typing import Any, Optional, NoReturn, List

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

    async def _find_one(
            self,
            obj_id: str,
            file_extension: str = None,
            parse_callback=None,
            directory_name: str = None,
    ) -> Any:
        file_name = obj_id
        if file_extension is not None:
            file_name = f'{file_name}.{file_extension}'
        bucket_name = self.get_bucket_name()

        if directory_name is None:
            directory_name = self.get_directory_name()

        response = self.__client.get_object(bucket_name, file_name)
        encoded_data = io.BytesIO(response.read()).getvalue()
        decoded_data = encoded_data.decode('utf-8')
        if parse_callback is not None:
            decoded_data = parse_callback(decoded_data)
        return decoded_data

    async def _create(
            self,
            obj_id: str,
            obj: Any,
            file_extension: str = None,
            directory_name: str = None,
            codification: str = 'utf-8',
    ) -> NoReturn:
        content: Optional[str] = None
        if isinstance(obj, str) or isinstance(obj, bytes):
            content = obj
        if isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, int):
            content = str(obj)
        if isinstance(obj, list) or isinstance(obj, dict):
            content = json.dumps(obj)
        if content is None:
            raise NotImplementedError('Not implementd error to raise')  # TODO: add custom error

        file_name = obj_id
        if file_extension is not None:
            file_name = f'{file_name}.{file_extension}'

        if directory_name is None:
            directory_name = self.get_directory_name()

        if directory_name is not None:
            file_name = f'{directory_name}/{file_name}'

        encoded_content = obj
        if isinstance(obj, str):
            encoded_content = content.encode(codification)
        to_stream_content = io.BytesIO(encoded_content)

        bucket_name = self.get_bucket_name()
        self.__client.put_object(bucket_name, file_name, to_stream_content, len(encoded_content))
