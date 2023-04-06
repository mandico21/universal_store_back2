from dataclasses import dataclass

from src.domain.models.category import CategoryId


@dataclass
class CategoryNewDTO:
    id: CategoryId
    name: str
    description: str | None
    parent_id: CategoryId | None
