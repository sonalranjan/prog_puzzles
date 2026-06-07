import asyncio
import logging
import time
from collections import OrderedDict

from base import LRUCacheBase

log = logging.getLogger(__name__)


class TTLLRUCache(LRUCacheBase):
    def __init__(self, capacity, ttl_seconds):
        self._cap = capacity
        self._ttl = ttl_seconds
        self._cache = OrderedDict()  # key -> (value, expiry_time)
        self._reaper_task = None

    async def start(self):
        """Call once after construction to launch the background reaper."""
        self._reaper_task = asyncio.create_task(self._reap_expired())

    async def stop(self):
        if self._reaper_task:
            self._reaper_task.cancel()
            try:
                await self._reaper_task
            except asyncio.CancelledError:
                pass

    def reaper_status(self):
        if self._reaper_task is None:
            return "not started"
        if self._reaper_task.done():
            ex = self._reaper_task.exception()
            return f"crashed: {ex}" if ex else "finished"
        if self._reaper_task.cancelled():
            return "cancelled"
        return "running"

    async def _reap_expired(self):
        log.info("reaper started")
        while True:
            try:
                await asyncio.sleep(self._ttl / 2)
                now = time.time()
                expired = [k for k, (_, exp) in self._cache.items() if now > exp]
                if expired:
                    log.info(f"reaper evicting {len(expired)} keys: {expired}")
                for k in expired:
                    del self._cache[k]
            except asyncio.CancelledError:
                log.info("reaper stopped")
                raise
            except Exception as e:
                log.error(f"reaper error: {e}")

    def get(self, key):
        if key not in self._cache:
            return -1
        if self._is_expired(key):
            del self._cache[key]
            return -1
        self._cache.move_to_end(key)
        return self._cache[key][0]

    def put(self, key, value):
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = (value, time.time() + self._ttl)
        if len(self._cache) > self._cap:
            self._cache.popitem(last=False)

    def _is_expired(self, key):
        _, expiry = self._cache[key]
        return time.time() > expiry

    def print(self):
        print(list(self._cache.items()))
