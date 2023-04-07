from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from src.application.category.dto import CategoryNewDTO
from src.application.category.interactor.create_category import CreateCategory
from src.application.category.interfaces import CategoryGateway
from src.domain.models.category import CategoryId, Category
from src.domain.services.category import CategoryService

NEW_CATEGORY_ID = CategoryId(10000)
CATEGORY = Category(
    id=NEW_CATEGORY_ID,
    name='Мужская',
    description=None,
    parent_id=None,
    created_at=datetime(2000, 12, 31),
    updated_at=datetime(2000, 12, 31),
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
async def test_create_wish_access(db_gateway):
    data = CategoryNewDTO(
        id=NEW_CATEGORY_ID,
        name='Мужская',
        description=None,
        parent_id=None,
    )
    res = await CreateCategory(db_gateway, CategoryService())(data)
    assert res == NEW_CATEGORY_ID  # Готово
