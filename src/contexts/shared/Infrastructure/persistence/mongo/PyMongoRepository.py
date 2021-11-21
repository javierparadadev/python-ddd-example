from abc import ABC, abstractmethod
from typing import Any, Dict

from pymongo import MongoClient

from src.contexts.shared.Infrastructure.persistence.mongo.parse_criteria_to_mongo_query import \
    parse_criteria_to_mongo_query
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoRepository(ABC):

    def __init__(self, client: MongoClient):
        self.__client = client
        self.__database = self.__client.get_database(self.get_database_name())
        self._collection = self.__database.get_collection(self.get_collection_name())

    @abstractmethod
    def get_database_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_collection_name(self):
        raise NotImplementedError()

    def _get_collection(self):
        return self._collection

    async def _find_one(self, raw_query: Dict[str, Any]) -> Any:
        return self._collection.find_one(raw_query)

    async def _find_many(self, raw_query: Dict[str, Any]) -> Any:
        cursor = self._collection.find(raw_query)
        data = list(cursor)
        return data

    async def _find_by_criteria(self, criteria: Criteria) -> Any:
        raw_query = parse_criteria_to_mongo_query(criteria)
        return await self._find_many(raw_query)

    async def _create_one(self, raw_obj: Dict[str, Any]) -> Any:
        self._collection.insert_one(raw_obj)
