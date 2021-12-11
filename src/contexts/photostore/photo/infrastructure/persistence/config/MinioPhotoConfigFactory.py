import json

from src.contexts.shared.Infrastructure.environment.EnvManager import EnvManager
from src.contexts.shared.Infrastructure.environment.EnvVar import EnvVar
from src.contexts.shared.Infrastructure.persistence.minio.MinioConfiguration import MinioConfiguration


class MinioPhotoConfigFactory:

    @staticmethod
    def create() -> MinioConfiguration:
        config = MinioConfiguration(
            host=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_HOST),
            port=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_PORT, parser=int),
            access_key=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_ACCESS_KEY),
            secret_key=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_SECRET_KEY),
            region=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_REGION),
            secure=EnvManager.get(EnvVar.SHARED_PHOTO_MINIO_SECURE, parser=json.loads),
        )
        return config
