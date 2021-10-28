from typing import List

from src.contexts.shared.domain.criteria.Filter import Filter
from src.contexts.shared.domain.criteria.OrderBy import OrderBy


class Criteria:

    def __init__(
            self,
            filters: List[Filter] = None,
            order: OrderBy = None,
    ):
        self.filters = filters
        self.order = order
