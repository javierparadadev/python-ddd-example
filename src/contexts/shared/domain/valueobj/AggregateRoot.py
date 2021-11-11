from abc import abstractmethod, ABC
from typing import Dict, List, Union

from src.contexts.shared.domain.DomainEvent import DomainEvent


class AggregateRoot(ABC):

    def __init__(self):
        self.__domain_events: List[DomainEvent] = []

    @abstractmethod
    def to_primitives(self) -> Union[Dict, List]:
        raise NotImplementedError()

    def pull_domain_events(self):
        events = self.__domain_events
        self.__domain_events = []
        return events

    def record_event(self, event: DomainEvent):
        self.__domain_events.append(event)
