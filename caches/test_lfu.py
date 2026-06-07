from base import LRUCacheBase
from lfu_cache import LFUCache


def test_lfu():
    cache: LRUCacheBase = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1       # freq: key=1 freq=2, key=2 freq=1
    cache.put(3, 3)                # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)                # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    cache.print()


if __name__ == "__main__":
    test_lfu()
    print("ok")
