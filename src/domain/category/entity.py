from dataclasses import dataclass

from src.domain.common.constants import Empty
from src.domain.common.entities import EntityMerge, Entity


@dataclass
class Category(Entity, EntityMerge):
    id: int
    name: str
    description: str | None
    parent_id: int | None

    @staticmethod
    def create(category_id: int,
               name: str,
               description: str | None,
               parent_id: int | None) -> 'Category':
        return Category(category_id, name, description, parent_id)

    def update(self,
               name: str | Empty = Empty.UNSET,
               description: str | Empty = Empty.UNSET,
               parent_id: int | Empty = Empty.UNSET) -> None:
        if name is not Empty.UNSET:
            self.name = name
        if description is not Empty.UNSET:
            self.description = description
        if parent_id is not Empty.UNSET:
            self.parent_id = parent_id
        self._merge(name=self.name, description=self.description, parent_id=self.parent_id)
