from typing import Protocol, List

from src.domain.category.dto import CategoryDTO
from src.domain.category.entity import Category


class ICategoryReader(Protocol):

    async def find_all(self) -> List[CategoryDTO]:
        ...

    async def find_by_id(self, category_id: int) -> CategoryDTO:
        ...


class ICategoryRepo(Protocol):

    async def add_category(self, category: Category) -> Category:
        ...

    async def find_by_id(self, category_id: int) -> Category:
        ...

    async def edit_category(self, category: Category) -> Category:
        ...

