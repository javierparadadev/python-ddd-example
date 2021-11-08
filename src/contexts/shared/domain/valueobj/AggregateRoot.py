from abc import abstractmethod, ABC
from typing import Optional, Dict, List, Union


class AggregateRoot(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_primitives(self) -> Union[Dict, List]:
        raise NotImplementedError()
