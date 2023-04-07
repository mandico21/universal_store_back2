from typing import Protocol, List

from src.application.common.interfaces import Transactional
from src.domain.models.category import CategoryId, Category


class CategoryCommand(Protocol):

    async def add_category(self, category: Category) -> CategoryId:
        raise NotImplementedError

    async def update_category(self, category: Category) -> None:
        raise NotImplementedError


class CategoryQuery(Protocol):

    async def find_all(self) -> List[Category]:
        raise NotImplementedError

    async def find_by_id(self, category_id: CategoryId) -> Category:
        raise NotImplementedError


class CategoryGateway(Transactional, CategoryCommand, CategoryQuery, Protocol):
    pass
