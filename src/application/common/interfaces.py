from typing import Protocol


class Comitter(Protocol):

    def commit(self) -> None:
        raise NotImplementedError


class Rollbacker(Protocol):

    def rollback(self) -> None:
        raise NotImplementedError


class Transactional(Comitter, Rollbacker, Protocol):
    pass
