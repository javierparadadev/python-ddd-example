from abc import abstractmethod
from typing import List

from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventSubscriber import EventSubscriber
from src.contexts.shared.domain.Interface import Interface


class EventBus(Interface):

    @abstractmethod
    async def publish(self, events: List[DomainEvent]):
        raise NotImplementedError()

    @abstractmethod
    def add_subscribers(self, subscribers: List[EventSubscriber]):
        raise NotImplementedError()

    @abstractmethod
    def start(self):
        raise NotImplementedError()
