from typing import Protocol

from src.application.common.interfaces import CategorySaver, CategoryReader, Transactional


class DbGateway(Transactional, CategoryReader, CategorySaver, Protocol):
    pass
