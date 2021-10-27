from abc import abstractmethod, ABC
from typing import Optional, Dict, List


class AggregateRoot(ABC):

    @abstractmethod
    def to_primitives(self) -> Optional[Dict, List]:
        raise NotImplementedError()
