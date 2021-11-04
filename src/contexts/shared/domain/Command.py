from abc import abstractmethod

from src.contexts.shared.domain.Interface import Interface


class Command(Interface):

    @abstractmethod
    def get_command_type_name(self) -> str:
        raise NotImplementedError()
