from src.domain.common.interfaces import IUoW
from .persistence import ICategoryReader, ICategoryRepo


class ICategoryUoW(IUoW):
    category: ICategoryRepo
    category_reader: ICategoryReader
