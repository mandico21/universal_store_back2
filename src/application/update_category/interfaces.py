from typing import Protocol

from src.application.common.interfaces import Transactional, CategoryGetable, CategorySaver


class DbGateway(Transactional, CategoryGetable, CategorySaver, Protocol):
    pass
