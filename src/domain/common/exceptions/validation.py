from dataclasses import dataclass

from src.domain.common.exceptions import DomainException


@dataclass
class BaseModelException(DomainException):
    field: str


@dataclass
class EmptyField(BaseModelException):

    def message(self):
        return f'Ошибка валидации: значение в поле {self.field} является пустой строкой, или состоит из пробелов'
