from typing import Any, Dict, List, Tuple, Optional

from src.contexts.shared.domain.criteria.Filter import Filter
from src.contexts.shared.domain.criteria.FilterField import FilterField
from src.contexts.shared.domain.criteria.FilterOperator import FilterOperator, FilterOperatorValues
from src.contexts.shared.domain.criteria.FilterValue import FilterValue
from src.contexts.shared.domain.criteria.Limit import Limit
from src.contexts.shared.domain.criteria.LimitOffset import LimitOffset
from src.contexts.shared.domain.criteria.OrderAttribute import OrderAttribute
from src.contexts.shared.domain.criteria.OrderBy import OrderBy
from src.contexts.shared.domain.criteria.OrderDirection import OrderDirection
from src.contexts.shared.domain.criteria.UpperLimit import UpperLimit


def parse_dict_to_criteria(query: Dict[str, Any]) -> Tuple[List[Filter], Optional[OrderBy], Optional[Limit]]:
    filters: List[Filter] = []
    order: Optional[OrderBy] = None
    limit: Optional[Limit] = None

    for key, value in query.items():
        if key.startswith('$'):
            if order is None and key.startswith('$ord'):
                attribute_name = query.get('$ord')
                if attribute_name is None:
                    continue
                order_direction = query.get('$dir')
                if order_direction is None:
                    order_direction = 'desc'
                order = OrderBy(OrderAttribute(attribute_name), OrderDirection(order_direction))
                continue

            if limit is None and key in ['$limit', '$offset']:
                upper_limit = query.get('$limit')
                lower_limit = query.get('$offset')
                if upper_limit is None:
                    upper_limit = 50
                if lower_limit is None:
                    lower_limit = 0
                limit = Limit(LimitOffset(lower_limit), UpperLimit(upper_limit))
                continue

            if limit is None and key == '$page':
                page = int(query.get('$page'))
                upper_limit = 50
                lower_limit = page * upper_limit
                limit = Limit(LimitOffset(lower_limit), UpperLimit(upper_limit))
                continue
            continue

        filter_field = FilterField(key)
        filter_operator = FilterOperator(FilterOperatorValues.EQUALS.value)
        filter_value = FilterValue(value)
        criteria_filter = Filter(filter_field, filter_operator, filter_value)
        filters.append(criteria_filter)

    return filters, order, limit
