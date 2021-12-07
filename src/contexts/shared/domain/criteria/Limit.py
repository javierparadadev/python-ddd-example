from src.contexts.shared.domain.criteria import UpperLimit
from src.contexts.shared.domain.criteria.LimitOffset import LimitOffset


class Limit:

    def __init__(self, lower: LimitOffset, upper: UpperLimit):
        self.lower = lower
        self.upper = upper
