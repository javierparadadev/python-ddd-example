from abc import ABC
from typing import List, NoReturn

from src.contexts.photostore.photo.domain.entities.Photo import Photo


class PhotoRepository(ABC):

    async def create_one(self, photo: Photo) -> NoReturn:
        raise NotImplementedError()
