import pytest as pytest

from src.domain.category.dto import CategoryCreateDTO
from src.domain.category.entity import Category
from src.domain.category.interfaces import ICategoryUoW
from src.domain.category.use_case import CategoryService
from src.domain.common.interfaces import IMapper


@pytest.fixture
def category():
    return Category.create(1, 'Мужская', 'Пустое', None)


@pytest.fixture
def category_create_dto():
    return CategoryCreateDTO(1, 'Мужская', 'Пустое', None)


def test_update(category):
    category_old = Category.create(1, 'Мужская', 'Пустое', None)
    category.update()
    assert category == category_old

    category.update(name='Женская')
    assert category != category_old
