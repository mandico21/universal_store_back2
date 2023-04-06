from dataclasses import dataclass
from datetime import datetime
from typing import NewType

CategoryId = NewType('CategoryId', int)


@dataclass
class Category:
    id: CategoryId
    name: str
    description: str | None
    parent_id: CategoryId | None
    created_at: datetime
    updated_at: datetime
