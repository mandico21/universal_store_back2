from src.application.common.interactor import UseCase
from src.application.create_category.dto import NewCategoryDTO, CategoryDTO
from src.application.create_category.interfaces import DbGateway
from src.domain.services.category import CategoryService


class CreateCategory(UseCase[NewCategoryDTO, CategoryDTO]):

    def __init__(self, db_gateway: DbGateway, category_service: CategoryService) -> None:
        self.db_gateway = db_gateway
        self.category_service = category_service

    def __call__(self, data: NewCategoryDTO) -> CategoryDTO:
        category = self.category_service.create_category(data)

        self.db_gateway.save_category(category)
        self.db_gateway.commit()
        return CategoryDTO(
            id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id,
            created_at=category.created_at,
            updated_at=category.updated_at
        )
