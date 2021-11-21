from typing import Any, Dict, List, Tuple, Optional

from src.contexts.shared.domain.criteria.Filter import Filter
from src.contexts.shared.domain.criteria.FilterField import FilterField
from src.contexts.shared.domain.criteria.FilterOperator import FilterOperator, FilterOperatorValues
from src.contexts.shared.domain.criteria.FilterValue import FilterValue
from src.contexts.shared.domain.criteria.OrderBy import OrderBy


def parse_dict_to_criteria(query: Dict[str, Any]) -> Tuple[List[Filter], Optional[OrderBy], Optional[Any]]:
    filters: List[Filter] = []
    for key, value in query.items():
        filter_field = FilterField(key)
        filter_operator = FilterOperator(FilterOperatorValues.EQUALS.value)
        filter_value = FilterValue(value)
        filter = Filter(filter_field, filter_operator, filter_value)
        filters.append(filter)
    return filters, None, None # TODO: add sort and order
