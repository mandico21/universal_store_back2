from src.application.common.interactor import UseCase
from src.application.update_category.dto import UpdateCategoryDTO
from src.application.update_category.exceptions import CategoryNotFoundError
from src.application.update_category.interfaces import DbGateway
from src.domain.models.category import CategoryId
from src.domain.services.category import CategoryService


class UpdateCategory(UseCase[UpdateCategoryDTO, None]):

    def __init__(
            self,
            db_gateway: DbGateway,
            category_service: CategoryService,
    ) -> None:
        self.db_gateway = db_gateway
        self.category_service = category_service

    def __call__(self, data: UpdateCategoryDTO) -> CategoryId:
        category = self.db_gateway.get_category(data.id)
        if not category:
            raise CategoryNotFoundError

        category_id = self.category_service.update_category(
            category,
            name=data.name,
            description=data.description,
            parent_id=data.parent_id
        )
        self.db_gateway.save_category(category)
        self.db_gateway.commit()
        return category_id
