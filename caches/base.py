from abc import ABC, abstractmethod

type KeyT = str
type ValueT = str


class LRUCacheBase(ABC):
    @abstractmethod
    def get(self, k: KeyT) -> ValueT | None:
        ...

    @abstractmethod
    def put(self, k: KeyT, v: ValueT) -> None:
        ...

    @abstractmethod
    def print(self) -> None:
        ...
