from http import HTTPStatus
from typing import Any, Dict, Optional

from starlette.responses import JSONResponse

from src.contexts.backoffice.users.domain.errors.UserAlreadyExistsError import UserAlreadyExistsError
from src.contexts.backoffice.users.domain.errors.UserInvalidValueError import UserInvalidValueError
from src.contexts.backoffice.users.domain.errors.UserNotFoundError import UserNotFoundError
from src.contexts.shared.domain.errors.DomainError import DomainError


class JsonResponseErrorHandler:

    __ERROR_OPTIONS_MAPPING: Dict[str, Dict[str, Any]] = {
        UserAlreadyExistsError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.CONFLICT,
        },
        UserInvalidValueError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.BAD_REQUEST,
        },
        UserNotFoundError.ERROR_ID: {
            'is-private': False,
            'is-critical': False,
            'status-code': HTTPStatus.NOT_FOUND,
        }
    }

    def __init__(self):
        pass

    def resolve(self, error: DomainError):
        error_options = None
        for error_id, options in self.__ERROR_OPTIONS_MAPPING.items():
            if error_id == error.get_id():
                error_options = options
                break
        if error_options is not None:
            status = error_options['status-code']
            content = error.to_primitives()
            if error_options['is-private']:
                del content['message']
            response = JSONResponse(
                status_code=status,
                content=content,
            )
            return response

        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
