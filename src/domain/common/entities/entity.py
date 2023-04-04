from abc import ABC, abstractmethod


class Entity(ABC):

    @abstractmethod
    def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, **kwargs):
        raise NotImplementedError


class EntityMerge:

    def _merge(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if isinstance(v, list):
                kwargs[k] = self.__dict__[k] + v
            elif isinstance(v, dict):
                kwargs[k] = {**self.__dict__[k], **v}
        self.__dict__ = {**self.__dict__, **kwargs}
