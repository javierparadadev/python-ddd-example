from abc import abstractmethod
from typing import Union, Dict, List


class DomainError(BaseException):

    @abstractmethod
    def to_primitives(self) -> Union[Dict, List]:
        raise NotImplementedError()

    @abstractmethod
    def get_id(self) -> str:
        raise NotImplementedError()
