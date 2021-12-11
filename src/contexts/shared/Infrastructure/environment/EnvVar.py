from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # -------------------- BACKOFFICE -----------------------
    # -------------------------------------------------------

    BACKOFFICE_SERVER_HOST = 'backoffice.server.host'
    BACKOFFICE_SERVER_PORT = 'backoffice.server.port'

    # -------------------------------------------------------
    # -------------------- PHOTO STORE ----------------------
    # -------------------------------------------------------

    PHOTOSTORE_SERVER_HOST = 'photostore.server.host'
    PHOTOSTORE_SERVER_PORT = 'photostore.server.port'

    # -------------------------------------------------------
    # ----------------------- USER --------------------------
    # -------------------------------------------------------

    SHARED_USER_MONGO_HOST = 'shared.user.mongo_host'
    SHARED_USER_MONGO_PORT = 'shared.user.mongo_port'

    # -------------------------------------------------------
    # ---------------------- PHOTO -------------------------
    # -------------------------------------------------------

    SHARED_PHOTO_MINIO_HOST       = 'shared.photo.minio_host'
    SHARED_PHOTO_MINIO_PORT       = 'shared.photo.minio_port'
    SHARED_PHOTO_MINIO_ACCESS_KEY = 'shared.photo.minio_access_key'
    SHARED_PHOTO_MINIO_SECRET_KEY = 'shared.photo.minio_secret_key'
    SHARED_PHOTO_MINIO_REGION     = 'shared.photo.minio_region'
    SHARED_PHOTO_MINIO_SECURE     = 'shared.photo.minio_secure'

    # -------------------------------------------------------
    # ------------------ PHOTO REGISTRY ---------------------
    # -------------------------------------------------------

    SHARED_PHOTO_REGISTRY_MONGO_HOST = 'shared.photo_registry.mongo_host'
    SHARED_PHOTO_REGISTRY_MONGO_PORT = 'shared.photo_registry.mongo_port'
