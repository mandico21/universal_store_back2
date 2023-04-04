from typing import Protocol

from src.application.common.interfaces import Comitter, CategorySaver, CategoryReader


class DbGateway(Comitter, CategoryReader, CategorySaver, Protocol):
    pass
