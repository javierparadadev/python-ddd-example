from typing import Any, Dict, List, Tuple, Optional

from src.contexts.shared.domain.criteria.Filter import Filter
from src.contexts.shared.domain.criteria.FilterField import FilterField
from src.contexts.shared.domain.criteria.FilterOperator import FilterOperator, FilterOperatorValues
from src.contexts.shared.domain.criteria.FilterValue import FilterValue
from src.contexts.shared.domain.criteria.OrderAttribute import OrderAttribute
from src.contexts.shared.domain.criteria.OrderBy import OrderBy
from src.contexts.shared.domain.criteria.OrderDirection import OrderDirection


def parse_dict_to_criteria(query: Dict[str, Any]) -> Tuple[List[Filter], Optional[OrderBy], Optional[Any]]:
    filters: List[Filter] = []
    order: Optional[OrderBy] = None
    for key, value in query.items():
        if key.startswith('$'):
            if order is None and key.startswith('$ord'):
                attribute_name = query.get('$ord')
                if attribute_name is None:
                    continue
                order_direction = query.get('$orddir')
                if order_direction is None:
                    order_direction = 'desc'
                order = OrderBy(OrderAttribute(attribute_name), OrderDirection(order_direction))
            continue

        filter_field = FilterField(key)
        filter_operator = FilterOperator(FilterOperatorValues.EQUALS.value)
        filter_value = FilterValue(value)
        filter = Filter(filter_field, filter_operator, filter_value)
        filters.append(filter)

    return filters, order, None  # TODO: add pagination
