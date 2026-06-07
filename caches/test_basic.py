from base import LRUCacheBase
from lru_cache import LRUCache


def test0():
    cache: LRUCacheBase = LRUCache(capacity=2)
    cache.print()
    cache.put(1, 1)   # cache: {1=1}
    cache.print()
    cache.put(2, 2)   # cache: {1=1, 2=2}
    cache.print()
    cache.get(1)      # returns 1; cache order: {2=2, 1=1}  (1 is now MRU)
    cache.print()
    cache.put(3, 3)   # evicts key 2 (LRU); cache: {1=1, 3=3}
    cache.print()
    cache.get(2)      # returns -1 (not found)
    cache.print()


if __name__ == "__main__":
    test0()
