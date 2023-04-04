from typing import Protocol

from src.domain.models.category import Category, CategoryId


class Comitter(Protocol):

    def commit(self):
        raise NotImplementedError


class CategoryReader(Protocol):

    def get_category(self, category_id: CategoryId) -> Category:
        raise NotImplementedError


class CategorySaver(Protocol):

    def save_category(self, category: Category) -> None:
        raise NotImplementedError
