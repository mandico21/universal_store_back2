import pytest as pytest

from src.domain.category.entity import Category


@pytest.fixture
def category():
    return Category.create(1, 'Мужская', 'Пустое')


def test_update(category):
    category_old = Category.create(1, 'Мужская', 'Пустое')
    category.update()
    print(category)
    assert category == category_old
    category.update(name='Женская')
    print(category)
    assert category != category_old

