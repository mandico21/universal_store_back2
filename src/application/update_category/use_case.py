from src.application.common.use_case import UseCase
from src.application.update_category.dto import UpdateCategoryDTO, CategoryDTO
from src.application.update_category.exceptions import CategoryNotFoundError
from src.application.update_category.interfaces import DbGateway
from src.domain.services.category import CategoryService


class UpdateCategory(UseCase[UpdateCategoryDTO, CategoryDTO]):

    def __init__(
            self,
            db_gateway: DbGateway,
            category_service: CategoryService,
    ) -> None:
        self.db_gateway = db_gateway
        self.category_service = category_service

    def __call__(self, data: UpdateCategoryDTO) -> CategoryDTO:
        category = self.db_gateway.get_category(data.id)
        if not category:
            raise CategoryNotFoundError

        update_category = self.category_service.update_category(
            category,
            name=data.name,
            description=data.description,
            parent_id=data.parent_id
        )
        self.db_gateway.commit()
        return CategoryDTO(
            id=update_category.id,
            name=update_category.name,
            description=update_category.description,
            parent_id=update_category.parent_id,
            created_at=update_category.created_at,
            updated_at=update_category.updated_at
        )
