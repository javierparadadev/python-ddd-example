from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # -------------------- BACKOFFICE -----------------------
    # -------------------------------------------------------

    BACKOFFICE_USER_MONGO_HOST = 'backoffice.user.mongo_host'
    BACKOFFICE_USER_MONGO_PORT = 'backoffice.user.mongo_port'

    # -------------------------------------------------------
    # -------------------- PHOTO STORE ----------------------
    # -------------------------------------------------------

    PHOTOSTORE_PHOTO_MINIO_HOST       = 'photostore.photo.minio_host'
    PHOTOSTORE_PHOTO_MINIO_PORT       = 'photostore.photo.minio_port'
    PHOTOSTORE_PHOTO_MINIO_ACCESS_KEY = 'photostore.photo.minio_access_key'
    PHOTOSTORE_PHOTO_MINIO_SECRET_KEY = 'backoffice.photo.minio_secret_key'
    PHOTOSTORE_PHOTO_MINIO_REGION     = 'backoffice.photo.minio_region'
