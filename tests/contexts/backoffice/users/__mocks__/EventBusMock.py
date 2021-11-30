from typing import List

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventBus import EventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber


class EventBusMock(BaseObject, EventBus):

    def start(self):
        pass

    async def publish(self, events: List[DomainEvent]):
        pass

    def add_subscribers(self, subscribers: List[EventSubscriber]):
        pass
