from dataclasses import dataclass

from src.domain.common.constants import Empty
from src.domain.common.entities import EntityMerge, Entity


@dataclass
class Category(Entity, EntityMerge):
    id: int
    name: str
    description: str | None

    @staticmethod
    def create(category_id: int, name: str, description: str | None) -> 'Category':
        return Category(category_id, name, description)

    def update(self, name: str | Empty = Empty.UNSET, description: str | Empty = Empty.UNSET) -> None:
        if name is not Empty.UNSET:
            self.name = name
        if description is not Empty.UNSET:
            self.description = description
        self._merge(name=self.name, description=self.description)
