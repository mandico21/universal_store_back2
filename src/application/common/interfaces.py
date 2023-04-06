from typing import Protocol


class Comitter(Protocol):

    async def commit(self) -> None:
        raise NotImplementedError


class Rollbacker(Protocol):

    async def rollback(self) -> None:
        raise NotImplementedError


class Transactional(Comitter, Rollbacker, Protocol):
    pass
