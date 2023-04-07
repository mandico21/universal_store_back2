from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from src.application.category.interfaces import CategoryGateway
from src.application.category.update_category.dto import CategoryUpdateDTO
from src.application.category.update_category.interfactor import UpdateCategory
from src.domain.models.category import CategoryId, Category
from src.domain.services.category import CategoryService

NEW_CATEGORY_ID = CategoryId(10000)
DATA = CategoryUpdateDTO(
    id=NEW_CATEGORY_ID,
    name='Женская',
)


@pytest.fixture()
def db_gateway() -> CategoryGateway:
    gateway = Mock()
    gateway.commit = Mock()
    gateway.rollback = Mock()
    gateway.find_by_id = Mock(return_value=Category(
        id=NEW_CATEGORY_ID,
        name='Мужская',
        description='Одежда для мужчин',
        parent_id=None,
        created_at=datetime(2000, 12, 31),
        updated_at=datetime(2000, 12, 31),
    ))
    gateway.add_category = Mock(return_value=CategoryId)
    gateway.update_category = Mock()
    return gateway


def test_update_category(db_gateway):
    old_date = datetime.now() - timedelta(days=1)
    UpdateCategory(db_gateway=db_gateway, category_service=CategoryService())(DATA)
    category = db_gateway.find_by_id(NEW_CATEGORY_ID)

    assert category.name == 'Женская'
    assert category.description == 'Одежда для мужчин'
    assert category.updated_at > old_date
