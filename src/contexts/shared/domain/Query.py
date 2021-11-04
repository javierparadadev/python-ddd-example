from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Query(Interface):

    @abstractmethod
    def get_query_type_name(self) -> str:
        raise NotImplementedError()
