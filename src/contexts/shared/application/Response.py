from abc import ABC, abstractmethod


class Response(ABC):

    @abstractmethod
    def to_json(self):
        raise NotImplementedError()
