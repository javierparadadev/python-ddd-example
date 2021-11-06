from enum import Enum


class EnvVar(Enum):

    ENV_MODE = 'env_mode'

    # -------------------------------------------------------
    # -------------------- BACKOFFICE -----------------------
    # -------------------------------------------------------

    BACKOFFICE_USER_MONGO_HOST = 'backoffice.user.mongo_host'
    BACKOFFICE_USER_MONGO_PORT = 'backoffice.user.mongo_port'
