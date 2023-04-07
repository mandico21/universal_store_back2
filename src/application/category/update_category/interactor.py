from src.application.category.exceptions import CategoryNotFoundError, CategoryAlreadyExistsError
from src.application.category.interfaces import CategoryGateway
from src.application.category.update_category.dto import CategoryUpdateDTO
from src.application.common.exception import IntegrityViolationError
from src.application.common.interactor import Interactor
from src.domain.services.category import CategoryService


class UpdateCategory(Interactor[CategoryUpdateDTO, None]):

    def __init__(
            self,
            db_gateway: CategoryGateway,
            category_service: CategoryService,
    ) -> None:
        self.db_gateway = db_gateway
        self.category_service = category_service

    async def __call__(self, data: CategoryUpdateDTO) -> None:
        category = await self.db_gateway.find_by_id(data.id)
        if not category:
            raise CategoryNotFoundError

        self.category_service.update_category(
            category,
            name=data.name,
            description=data.description,
            parent_id=data.parent_id
        )
        try:
            await self.db_gateway.update_category(category)
            await self.db_gateway.commit()
        except IntegrityViolationError:
            await self.db_gateway.rollback()
            raise CategoryAlreadyExistsError
