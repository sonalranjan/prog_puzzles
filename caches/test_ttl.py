import asyncio
import logging
import time

from ttl_lru_cache import TTLLRUCache


async def test1():
    cache: TTLLRUCache = TTLLRUCache(capacity=2, ttl_seconds=3)
    await cache.start()
    print(cache.reaper_status())

    cache.print()
    cache.put(1, 1)   # cache: {1=1}
    await asyncio.sleep(1)
    cache.print()
    cache.put(2, 2)   # cache: {1=1, 2=2}
    await asyncio.sleep(1)
    cache.print()
    cache.get(1)      # returns 1; cache order: {2=2, 1=1}  (1 is now MRU)
    cache.print()
    cache.put(3, 3)   # evicts key 2 (LRU); cache: {1=1, 3=3}
    await asyncio.sleep(1)
    cache.print()
    cache.get(2)      # returns -1 (not found)
    cache.print()

    deadline = time.time() + 10
    while cache._cache and time.time() < deadline:
        await asyncio.sleep(1)
        print(cache.reaper_status())
        cache.print()

    await cache.stop()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(test1())
