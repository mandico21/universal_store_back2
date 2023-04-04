from datetime import datetime, timedelta

from src.domain.models.category import Category, CategoryId
from src.domain.services.category import CategoryService


def test_category_update():
    old_date = datetime.now() - timedelta(days=1)
    category = Category(
        id=CategoryId(1),
        name='Мужская',
        description=None,
        parent_id=None,
        created_at=old_date,
        updated_at=old_date,
    )

    CategoryService().update_category(category, name='Женская')
    assert category.name == 'Женская'
    assert category.description == None
    assert category.updated_at > old_date
