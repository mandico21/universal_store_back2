from dataclasses import dataclass
from datetime import datetime

from src.domain.models.category import CategoryId


@dataclass
class NewCategoryDTO:
    id: CategoryId
    name: str
    description: str | None
    parent_id: CategoryId | None


@dataclass
class CategoryDTO:
    id: CategoryId
    name: str
    description: str | None
    parent_id: CategoryId | None
    created_at: datetime
    updated_at: datetime
