from typing import List, NoReturn, Tuple, Optional

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.backoffice.users.domain.UserRepository import UserRepository
from src.contexts.backoffice.users.domain.entities.User import User
from src.contexts.backoffice.users.domain.errors.UserAlreadyExistsError import UserAlreadyExistsError
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoUserRepository(PyMongoRepository, UserRepository):

    __COLLECTION_NAME = 'users'
    __DATABASE_NAME = 'python-ddd-example'

    def __init__(self, client: MongoClient):
        super().__init__(client)
        super()._get_collection().create_index([
            ('id', ASCENDING)
        ], unique=True)

    def get_database_name(self):
        return self.__DATABASE_NAME

    def get_collection_name(self):
        return self.__COLLECTION_NAME

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[User], Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [User.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata

    async def create_one(self, user: User) -> NoReturn:
        try:
            user = await super()._create_one(user.to_primitives())
            return user
        except DuplicateKeyError as e:
            raise UserAlreadyExistsError('User with ID <{}> already exists.'.format(user.id.value()))
