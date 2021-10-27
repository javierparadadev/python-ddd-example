from typing import List

from src.contexts.shared.domain.criteria.Filter import Filter


class Criteria:

    def __init__(self, filters: List[Filter] = None):
        self.filters = filters
