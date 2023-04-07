# from datetime import datetime
# from unittest.mock import Mock
#
# import pytest
#
# from src.application.category.create_category.dto import CategoryNewDTO
# from src.application.category.create_category.interactor import CreateCategory
# from src.domain.models.category import CategoryId, Category
#
# NEW_CATEGORY_ID = CategoryId(10000)
# CATEGORY = CategoryDTO(
#     id=NEW_CATEGORY_ID,
#     name='Мужская',
#     description=None,
#     parent_id=None,
#     created_at=datetime(2000, 12, 31),
#     updated_at=datetime(2000, 12, 31),
# )
#
#
# @pytest.fixture()
# def db_gateway() -> DbGateway:
#     gateway = Mock()
#     gateway.commit = Mock()
#     gateway.save_category = Mock()
#     gateway.get_category = Mock(return_value=Category(
#         id=NEW_CATEGORY_ID,
#         name='Мужская',
#         description=None,
#         parent_id=None,
#         created_at=datetime(2000, 12, 31),
#         updated_at=datetime(2000, 12, 31),
#     ))
#     return gateway
#
#
# @pytest.fixture()
# def wish_service() -> Mock:
#     service = Mock()
#     service.create_category = Mock(return_value=Category(
#         id=NEW_CATEGORY_ID,
#         name='Мужская',
#         description=None,
#         parent_id=None,
#         created_at=datetime(2000, 12, 31),
#         updated_at=datetime(2000, 12, 31),
#     ))
#     service.update_category = Mock(
#         return_value=Category(
#             id=NEW_CATEGORY_ID,
#             name='Мужская',
#             description=None,
#             parent_id=None,
#             created_at=datetime(2000, 12, 31),
#             updated_at=datetime(2000, 12, 31),
#         )
#     )
#     return service
#
#
# def test_create_wish_access(db_gateway, wish_service):
#     usecase = CreateCategory(
#         db_gateway=db_gateway,
#         category_service=wish_service,
#     )
#     res = usecase(CategoryNewDTO(
#         id=NEW_CATEGORY_ID,
#         name='Мужская',
#         description=None,
#         parent_id=None,
#     ))
#     assert res == CATEGORY
