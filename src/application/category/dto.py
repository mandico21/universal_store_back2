from dataclasses import dataclass

from src.domain.models.category import CategoryId


@dataclass
class CategoryUpdateDTO:
    id: CategoryId
    name: str | None = None
    description: str | None = None
    parent_id: CategoryId | None = None


@dataclass
class CategoryNewDTO:
    id: CategoryId
    name: str
    description: str | None
    parent_id: CategoryId | None
