from typing import List

from src.contexts.photostore.photo.domain.entities.PhotoTag import PhotoTag
from src.contexts.shared.domain.valueobj.ValueObject import ValueObject


class PhotoTags(ValueObject):

    def __init__(self, value: List[PhotoTag]):
        super().__init__(value)

    def values(self):
        tags: List[PhotoTag] = self._value
        return [tag.value() for tag in tags]
