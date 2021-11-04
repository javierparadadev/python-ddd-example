from typing import Any

from src.contexts.shared.domain.Query import Query


class FindUsersByCriteriaQuery(Query):

    QUERY_TYPE: str = 'find-users-by-criteria'

    def __init__(self, raw_criteria: Any):
        self.raw_criteria = raw_criteria

    def get_query_type_name(self) -> str:
        return self.QUERY_TYPE
