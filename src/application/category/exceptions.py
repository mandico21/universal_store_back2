from src.application.common.exception import ApplicationError


class CategoryAlreadyExistsError(ApplicationError):
    pass


class CategoryNotFoundError(ApplicationError):
    pass
