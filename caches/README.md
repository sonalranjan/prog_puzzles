# Cache Implementations

LRU and LFU cache implementations, plus a TTL LRU variant with a background reaper for automatic expiry.

## Requirements

- Python 3.10+

## Project layout

```
prog_puzzles/caches/
├── base.py             # LRUCacheBase (get, put, print)
├── lru_cache.py        # LRUCache + LNode (doubly-linked list)
├── ttl_lru_cache.py    # TTLLRUCache (OrderedDict + async reaper)
├── lfu_cache.py        # LFUCache (LeetCode 460)
├── test_basic.py       # demo for linked-list LRU
├── test_ttl.py         # demo for TTL LRU + reaper
└── test_lfu.py         # demo for LFU
```

## Implementations

### `LRUCache` (basic)

Linked-list LRU with O(1) get and put. Evicts the least-recently-used entry when capacity is exceeded.

### `TTLLRUCache` (TTL)

OrderedDict-based LRU that also expires entries after a configurable TTL. A background asyncio task (the **reaper**) periodically scans and removes expired keys.

TTL-specific methods:

| Method | Description |
|--------|-------------|
| `await start()` | Launch the background reaper |
| `await stop()` | Cancel the reaper and wait for clean shutdown |
| `reaper_status()` | `"not started"`, `"running"`, `"finished"`, `"cancelled"`, or `"crashed: …"` |

### `LFUCache`

Least-frequently-used cache ([LeetCode 460](https://leetcode.com/problems/lfu-cache/)). Evicts the least-frequently-used key; ties broken by least-recently-used within the same frequency.

## Usage

```python
from base import LRUCacheBase
from lru_cache import LRUCache
from ttl_lru_cache import TTLLRUCache
from lfu_cache import LFUCache

# Basic LRU
cache: LRUCacheBase = LRUCache(capacity=100)
cache.put("a", "1")
cache.get("a")
cache.print()

# TTL LRU
ttl_cache = TTLLRUCache(capacity=100, ttl_seconds=60)
await ttl_cache.start()
ttl_cache.put("a", "1")
await ttl_cache.stop()

# LFU
lfu_cache = LFUCache(capacity=100)
lfu_cache.put(1, 1)
lfu_cache.get(1)
lfu_cache.print()
```

## Running the demos

From the `prog_puzzles/caches/` directory:

```bash
python3 test_basic.py
python3 test_ttl.py
python3 test_lfu.py
```

## Interface

`LRUCache`, `TTLLRUCache`, and `LFUCache` implement `LRUCacheBase`:

```python
def get(self, k: KeyT) -> ValueT | None: ...
def put(self, k: KeyT, v: ValueT) -> None: ...
def print(self) -> None: ...
```

Note: `LRUCache` returns `None` on miss; `TTLLRUCache` and `LFUCache` return `-1` (LeetCode convention).
