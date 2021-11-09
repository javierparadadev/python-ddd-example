import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Any


class DomainEvent(ABC):

    def __init__(
            self,
            name: str,
            aggregate_id: str,
            event_id: Optional[str],
            occurred_on: Optional[datetime]):
        self.name = name
        self.aggregate_id = aggregate_id
        if self.aggregate_id is None:
            self.aggregate_id = uuid.uuid4()
        self.id = event_id
        self.occurred_on = occurred_on
        self.created_at = datetime.now()
        if self.occurred_on is None:
            self.occurred_on = self.created_at

    def get_event_type_name(self) -> str:
        return self.name

    @abstractmethod
    def to_primitives(self) -> Any:
        raise NotImplementedError()
