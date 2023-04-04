from typing import Any, Protocol, TypeVar, Type

T = TypeVar("T")


class IMapper(Protocol):

    def load(self, class_: Type[T], data: Any) -> T:
        raise NotImplementedError
