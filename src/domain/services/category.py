from datetime import datetime

from src.application.create_category.dto import NewCategoryDTO
from src.domain.models.category import Category, CategoryId


class CategoryService:

    def create_category(self, category: NewCategoryDTO) -> Category:
        return Category(
            id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    def update_category(
            self,
            category: Category,
            name: str | None = None,
            description: str | None = None,
            parent_id: str | None = None
    ) -> CategoryId:
        if name is not None:
            category.name = name
        if description is not None:
            category.description = description
        if parent_id is not None:
            category.parent_id = parent_id

        category.updated_at = datetime.now()
        return category.id
