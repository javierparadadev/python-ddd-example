from typing import List

from pymongo import MongoClient

from src.contexts.backoffice.users.domain.BackofficeUserRepository import BackofficeUserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoBackofficeUserRepository(PyMongoRepository, BackofficeUserRepository):

    __COLLECTION_NAME = 'users'
    __DATABASE_NAME = 'backoffice'

    def __init__(self, client: MongoClient):
        super().__init__(client)

    def get_database_name(self):
        return self.__DATABASE_NAME

    def get_collection_name(self):
        return self.__COLLECTION_NAME

    async def find_by_criteria(self, criteria: Criteria) -> List[User]:
        return await super()._find_many({})