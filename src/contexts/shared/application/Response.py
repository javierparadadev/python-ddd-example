from abc import ABC, abstractmethod


class Response(ABC):

    @abstractmethod
    def to_primitives(self):
        raise NotImplementedError()


