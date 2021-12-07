from abc import ABC, abstractmethod


class Metadata(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError()
