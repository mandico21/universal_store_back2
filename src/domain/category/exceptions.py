from src.domain.common.exceptions import AppException


class CategoryException(AppException):
    ...


class CategoryAlreadyExists(CategoryException):
    ...


class CategoryNotExists(CategoryException):
    ...
