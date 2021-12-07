from uuid import UUID


class Uuid:

    @staticmethod
    def is_valid_uuid(content: str, version=4):
        try:
            uuid_obj = UUID(content, version=version)
        except ValueError:
            return False
        return str(uuid_obj) == content