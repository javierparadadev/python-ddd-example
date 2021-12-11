from typing import List, NoReturn, Tuple, Optional

from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError

from src.contexts.photostore.photoregistry.domain.PhotoRegistryRepository import PhotoRegistryRepository
from src.contexts.photostore.photoregistry.domain.entities.PhotoRegistry import PhotoRegistry
from src.contexts.photostore.photoregistry.domain.errors.PhotoAlreadyExistsError import PhotoRegistryAlreadyExistsError
from src.contexts.shared.Infrastructure.persistence.mongo.PyMongoRepository import PyMongoRepository
from src.contexts.shared.domain.CriteriaQueryMetadata import CriteriaQueryMetadata
from src.contexts.shared.domain.criteria.Criteria import Criteria


class PyMongoPhotoRegistryRepository(PyMongoRepository, PhotoRegistryRepository):

    __COLLECTION_NAME = 'photo-registry'
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

    async def find_by_criteria(self, criteria: Criteria) -> Tuple[List[PhotoRegistry], Optional[CriteriaQueryMetadata]]:
        results, count = await super()._find_by_criteria(criteria)
        entities = [PhotoRegistry.create_from_primitives(result) for result in results]
        metadata = CriteriaQueryMetadata(count)
        return entities, metadata

    async def create_one(self, registry: PhotoRegistry) -> NoReturn:
        try:
            registry = await super()._create_one(registry.to_primitives())
            return registry
        except DuplicateKeyError as e:
            raise PhotoRegistryAlreadyExistsError('User with ID <{}> already exists.'.format(registry.id.value()))
