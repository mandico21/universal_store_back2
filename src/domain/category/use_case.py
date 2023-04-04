from abc import ABC

from src.domain.category.dto import CategoryCreateDTO, CategoryDTO
from src.domain.category.entity import Category
from src.domain.category.exceptions import CategoryAlreadyExists, CategoryNotExists
from src.domain.category.interfaces import ICategoryUoW
from src.domain.common.exceptions.base import IntegrityViolationError
from src.domain.common.interfaces import IMapper


class CategoryUseCase(ABC):

    def __init__(self, uow: ICategoryUoW, mapper: IMapper) -> None:
        self.uow = uow
        self.mapper = mapper


class GetById(CategoryUseCase):

    async def __call__(self, category_id: int) -> CategoryDTO:
        category = await self.uow.category_reader.find_by_id(category_id)
        if not category:
            raise CategoryNotExists

        return self.mapper.load(CategoryDTO, category)


class AddCategory(CategoryUseCase):

    async def __call__(self, category: CategoryCreateDTO) -> CategoryDTO:
        if category.parent_id:
            parent = await self.uow.category_reader.find_by_id(category.parent_id)
            if not parent:
                raise CategoryNotExists

        category_new = Category.create(
            category_id=category.id,
            name=category.name,
            description=category.description,
            parent_id=category.parent_id
        )
        try:
            category = await self.uow.category.add_category(category_new)
            await self.uow.commit()
        except IntegrityViolationError:
            await self.uow.rollback()
            raise CategoryAlreadyExists
        return self.mapper.load(CategoryDTO, category)


class CategoryService:

    def __init__(self, uow: ICategoryUoW, mapper: IMapper) -> None:
        self.uow = uow
        self.mapper = mapper

    async def find_by_id(self, category_id: int) -> CategoryDTO:
        return await GetById(self.uow, self.mapper)(category_id)

    async def add_category(self, category: CategoryCreateDTO) -> CategoryDTO:
        return await AddCategory(self.uow, self.mapper)(category)
