from typing import Protocol

from src.application.common.interfaces import Transactional
from src.domain.models.category import CategoryId, Category


class CategoryGateway(Transactional, Protocol):

    async def add_category(self, category: Category) -> CategoryId:
        raise NotImplementedError

    async def find_by_id(self, category_id: CategoryId) -> Category:
        raise NotImplementedError

    async def update_category(self, category: Category) -> None:
        raise NotImplementedError
