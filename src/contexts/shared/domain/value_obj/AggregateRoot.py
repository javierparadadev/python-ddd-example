from abc import abstractmethod, ABC
from typing import Optional, Dict, List


class AggregateRoot(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_primitives(self) -> Optional[Dict, List]:
        raise NotImplementedError()
