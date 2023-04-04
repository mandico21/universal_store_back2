from typing import Protocol

from src.application.common.interfaces import Transactional, CategoryReader, CategorySaver


class DbGateway(Transactional, CategoryReader, CategorySaver, Protocol):
    pass
