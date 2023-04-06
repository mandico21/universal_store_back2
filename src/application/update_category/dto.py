from dataclasses import dataclass

from src.domain.models.category import CategoryId


@dataclass
class UpdateCategoryDTO:
    id: CategoryId
    name: str | None = None
    description: str | None = None
    parent_id: CategoryId | None = None
