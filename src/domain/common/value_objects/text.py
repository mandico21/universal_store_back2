from src.domain.common.exceptions import EmptyField
from src.domain.common.value_objects import ValueObject


class TextVO(ValueObject):
    value: str

    def __post_init__(self) -> None:
        if not self.value or self.value.isspace():
            raise EmptyField(self.__field_name__)

    def to_string(self) -> str:
        return self.value
