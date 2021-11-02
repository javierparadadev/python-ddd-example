import logging
from typing import Any

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.logger.Logger import Logger


class NativeConsoleLogger(BaseObject, Logger):

    __FORMAT = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.__FORMAT)
        self.__logger.addHandler(console_handler)

    def debug(self, log: Any):
        self.__logger.debug(log)

    def info(self, log: Any):
        self.__logger.info(log)

    def error(self, log: Any):
        self.__logger.error(log)

    def critical(self, log: Any):
        self.__logger.critical(log)
