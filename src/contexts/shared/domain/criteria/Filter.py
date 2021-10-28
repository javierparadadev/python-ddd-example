from src.contexts.shared.domain.criteria.FilterField import FilterField
from src.contexts.shared.domain.criteria.FilterOperator import FilterOperator
from src.contexts.shared.domain.criteria.FilterValue import FilterValue


class Filter:

    def __init__(self, field: FilterField, operator: FilterOperator, value: FilterValue):
        self.field = field
        self.operator = operator
        self.value = value
