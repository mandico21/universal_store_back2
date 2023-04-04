class AppException(Exception):
    """Base Exception"""

    @property
    def message(self) -> str:
        ...


class DomainException(AppException):
    """Base Domain Exception"""
