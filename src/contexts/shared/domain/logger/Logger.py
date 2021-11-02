from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Logger(Interface):

    @abstractmethod
    def debug(self):
        raise NotImplementedError()

    @abstractmethod
    def info(self):
        raise NotImplementedError()

    @abstractmethod
    def error(self):
        raise NotImplementedError()

    @abstractmethod
    def critical(self):
        raise NotImplementedError()
