from abc import ABC
from typing import NoReturn

from src.contexts.photostore.photoregistry.domain.entities.PhotoRegistry import PhotoRegistry


class PhotoRegistryRepository(ABC):

    async def create_one(self, photo_registry: PhotoRegistry) -> NoReturn:
        raise NotImplementedError()
