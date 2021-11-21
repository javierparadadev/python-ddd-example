from typing import Any, Dict

from src.contexts.shared.domain.criteria.Criteria import Criteria


def parse_criteria_to_mongo_query(criteria: Criteria) -> Dict[str, Any]:
    raw_query = {}
    for filter in criteria.filters:
        raw_query[filter.field.value] = filter.value.value
    return raw_query
