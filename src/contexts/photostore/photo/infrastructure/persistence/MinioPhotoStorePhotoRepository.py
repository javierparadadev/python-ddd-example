from typing import NoReturn

from pymongo.errors import DuplicateKeyError

from src.contexts.photostore.photo.domain.PhotoRepository import PhotoRepository
from src.contexts.photostore.photo.domain.entities.Photo import Photo
from src.contexts.photostore.photo.domain.errors.PhotoAlreadyExistsError import PhotoAlreadyExistsError
from src.contexts.shared.Infrastructure.persistence.minio.MinioRepository import MinioRepository


class MinioPhotoRepository(MinioRepository, PhotoRepository):

    __BUCKET_NAME = 'photos'
    __DIRECTORY_DEFAULT_NAME = ''

    def get_bucket_name(self):
        return MinioPhotoRepository.__BUCKET_NAME

    def get_directory_name(self):
        return MinioPhotoRepository.__DIRECTORY_DEFAULT_NAME

    async def create_one(self, photo: Photo) -> NoReturn:
        try:
            photo = await super()._create(
                obj_id=photo.id.value(),
                obj={},
                file_extension='jpg',
                directory_name=photo.user_id.value(),
            )
            return photo
        except DuplicateKeyError as e:
            raise PhotoAlreadyExistsError('Photo with ID <{}> already exists.'.format(photo.id.value()))