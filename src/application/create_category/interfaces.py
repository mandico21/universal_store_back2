from typing import Protocol

from src.application.common.interfaces import CategorySaver, CategoryGetable, Transactional


class DbGateway(Transactional, CategoryGetable, CategorySaver, Protocol):
    pass
