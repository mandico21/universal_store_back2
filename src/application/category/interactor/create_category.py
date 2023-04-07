from src.application.category.dto import CategoryNewDTO
from src.application.category.exceptions import CategoryAlreadyExistsError

from src.application.category.interfaces import CategoryGateway
from src.application.common.exception import IntegrityViolationError
from src.application.common.interactor import Interactor
from src.domain.models.category import CategoryId
from src.domain.services.category import CategoryService


class CreateCategory(Interactor[CategoryNewDTO, CategoryId]):

    def __init__(
            self,
            db_gateway: CategoryGateway,
            category_service: CategoryService
    ) -> None:
        self.db_gateway = db_gateway
        self.category_service = category_service

    async def __call__(self, data: CategoryNewDTO) -> CategoryId:
        category = self.category_service.create_category(category=data)
        try:
            await self.db_gateway.add_category(category=category)
            await self.db_gateway.commit()
        except IntegrityViolationError:
            await self.db_gateway.rollback()
            raise CategoryAlreadyExistsError
        return category.id
