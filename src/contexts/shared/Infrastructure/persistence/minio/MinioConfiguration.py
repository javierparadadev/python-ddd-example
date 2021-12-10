from minio import Minio


class MinioConfiguration:

    def __init__(
            self,
            host: str = 'localhost',
            port: int = 9000,
            access_key: str = None,
            secret_key: str = None,
            region: str = None,
            secure: bool = False,
    ):
        self.host = host
        self.port = port
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.secure = secure

    def create_client_from_config(self) -> Minio:
        return Minio(
            f'{self.host}:{self.port}',
            access_key=self.access_key,
            secret_key=self.secret_key,
            region=self.region,
            secure=self.secure,
        )
