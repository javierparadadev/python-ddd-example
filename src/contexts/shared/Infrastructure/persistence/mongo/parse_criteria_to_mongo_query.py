from typing import Any, Dict, Tuple

from src.contexts.shared.domain.criteria.Criteria import Criteria


def parse_criteria_to_mongo_query(criteria: Criteria) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    raw_query = {}
    options = {}

    for query_filter in criteria.filters:
        raw_query[query_filter.field.value] = query_filter.value.value

    if criteria.order is not None:
        options['sort'] = criteria.order.attribute.value

    if criteria.limit is not None:
        options['limit'] = criteria.limit.upper.value
        options['skip'] = criteria.limit.lower.value

    return raw_query, options
