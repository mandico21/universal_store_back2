class AppException(Exception):
    """Base Exception"""

    @property
    def message(self) -> str:
        return "An application error occurred"


class DomainException(AppException):
    """Base Domain Exception"""


class UnexpectedError(AppException):
    pass


class CommitError(UnexpectedError):
    pass


class RollbackError(UnexpectedError):
    pass


class RepoError(UnexpectedError):
    pass


class IntegrityViolationError(RepoError):
    """Violation of constraint"""
