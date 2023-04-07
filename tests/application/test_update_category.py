from datetime import datetime, timedelta
from unittest.mock import Mock, AsyncMock

import pytest

from src.application.category.interfaces import CategoryGateway
from src.application.category.update_category.dto import CategoryUpdateDTO
from src.application.category.update_category.interactor import UpdateCategory
from src.domain.models.category import CategoryId, Category
from src.domain.services.category import CategoryService

NEW_CATEGORY_ID = CategoryId(10000)
DATA = CategoryUpdateDTO(
    id=NEW_CATEGORY_ID,
    name='Женская',
)
DATA_ERROR = CategoryUpdateDTO(
    id=CategoryId(1002),
    name='Женская',
)


@pytest.fixture()
def db_gateway() -> CategoryGateway:
    gateway = AsyncMock()
    gateway.commit = AsyncMock()
    gateway.rollback = AsyncMock()
    gateway.find_by_id = AsyncMock(return_value=Category(
        id=NEW_CATEGORY_ID,
        name='Мужская',
        description='Одежда для мужчин',
        parent_id=None,
        created_at=datetime(2000, 12, 31),
        updated_at=datetime(2000, 12, 31),
    ))
    gateway.add_category = AsyncMock(return_value=CategoryId)
    gateway.update_category = AsyncMock()
    return gateway


@pytest.mark.asyncio
async def test_update_category_access(db_gateway):
    old_date = datetime.now() - timedelta(days=1)
    await UpdateCategory(db_gateway=db_gateway, category_service=CategoryService())(DATA)
    category = await db_gateway.find_by_id(NEW_CATEGORY_ID)

    assert category.name == 'Женская'
    assert category.description == 'Одежда для мужчин'
    assert category.updated_at > old_date
