from dataclasses import dataclass

from src.domain.common.dto import DTO


@dataclass
class BaseCategoryDTO(DTO):
    id: int


@dataclass
class CategoryCreateDTO(BaseCategoryDTO):
    name: str
    description: str | None
    parent_id: int | None


@dataclass
class CategoryDTO(BaseCategoryDTO):
    name: str
    description: str | None
    parent_id: int | None
