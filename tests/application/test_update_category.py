from datetime import datetime
from unittest.mock import Mock

import pytest

from src.application.category.interfaces import CategoryGateway
from src.application.category.update_category.dto import CategoryUpdateDTO
from src.application.category.update_category.interfactor import UpdateCategory
from src.domain.models.category import CategoryId, Category

NEW_CATEGORY_ID = CategoryId(10000)
# CATEGORY = CategoryNewDTO(
#     id=NEW_CATEGORY_ID,
#     name='Мужская',
#     description=None,
#     parent_id=None,
# )
DATA = CategoryUpdateDTO(
    id=NEW_CATEGORY_ID,
    name='Женская',
)


@pytest.fixture()
def db_gateway() -> CategoryGateway:
    gateway = Mock()
    gateway.commit = Mock()
    gateway.rollback = Mock()
    gateway.find_by_id = Mock()
    gateway.add_category = Mock(return_value=CategoryId)
    gateway.update_category = Mock()
    return gateway


@pytest.fixture()
def category_service() -> Mock:
    service = Mock()
    service.update_category = Mock()
    service.create_category = Mock(return_value=Category(
        id=NEW_CATEGORY_ID,
        name='Мужская',
        description=None,
        parent_id=None,
        created_at=datetime(2000, 12, 31),
        updated_at=datetime(2000, 12, 31),
    ))
    return service


def test_update_category(db_gateway, category_service):
    UpdateCategory(db_gateway=db_gateway, category_service=category_service)(DATA)

    print(db_gateway.find_by_id(NEW_CATEGORY_ID))
    print(DATA)
