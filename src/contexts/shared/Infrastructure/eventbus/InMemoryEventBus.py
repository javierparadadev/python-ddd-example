from typing import List, Dict

from src.contexts.shared.domain.BaseObject import BaseObject
from src.contexts.shared.domain.DomainEvent import DomainEvent
from src.contexts.shared.domain.EventBus import EventBus
from src.contexts.shared.domain.EventSubscriber import EventSubscriber


class InMemoryEventBus(BaseObject, EventBus):

    def __init__(self):
        self.__subscriptions: Dict[str, List[EventSubscriber]] = {}

    def start(self):
        pass

    async def publish(self, events: List[DomainEvent]):
        for event in events:
            event_type = event.get_event_type_name()
            if event_type not in self.__subscriptions:
                continue
            subscribers = self.__subscriptions[event_type]
            for subscriber in subscribers:
                await subscriber.on(event)  # TODO: add gather or future

    def add_subscribers(self, subscribers: List[EventSubscriber]):
        for subscriber in subscribers:
            event_types = subscriber.subscribed_to()
            for event_type in event_types:
                if event_type not in self.__subscriptions:
                    self.__subscriptions[event_type] = []
                self.__subscriptions[event_type].append(subscriber)
