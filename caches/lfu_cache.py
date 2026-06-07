from datetime import datetime

from base import KeyT, LRUCacheBase, ValueT

# https://leetcode.com/problems/lfu-cache/


class FreqNode:

    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

    def __repr__(self):
        return f"{self.data}"


class FreqList:

    def __init__(self):
        self._head = None
        self._tail = None

    def popleft(self):
        if not self._head:
            return None
        node = self._head
        nxt = node.next
        if nxt:
            nxt.prev = None
        self._head = nxt
        if self._tail == node:
            self._tail = nxt
        return node

    def find(self, data):
        node = self._head
        while node and node.data != data:
            node = node.next
        return node

    def append(self, data):
        node = FreqNode(data)
        if not self._head:
            self._head = node
            self._tail = node
            return node
        self._tail.next = node
        node.prev = self._tail
        self._tail = node
        return node

    def remove(self, data):
        node = self.find(data)
        if not node:
            return
        prev, nxt = node.prev, node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev
        node.prev = None
        node.next = None
        if self._head == node:
            self._head = nxt
        if self._tail == node:
            self._tail = prev

    def __repr__(self):
        parts = []
        node = self._head
        while node:
            parts.append(str(node))
            node = node.next
        return "->".join(parts)


class LFUEntry:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.use_count = 0
        self.ts = 0
        self.touch()

    def touch(self):
        self.use_count += 1
        self.ts = datetime.now().timestamp()

    def freq_key(self):
        return (self.use_count, self.ts, self.key)

    def __repr__(self):
        return f"key={self.key} use_count={self.use_count} ts={self.ts}"


class LFUCache(LRUCacheBase):

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._freq_lists = {}

    def get(self, key: KeyT) -> ValueT | None:
        if key not in self._cache:
            return -1
        entry = self._cache[key]
        old_key = entry.freq_key()
        entry.touch()
        new_key = entry.freq_key()
        self._update_freq_list(old_key, new_key)
        return entry.val

    def put(self, key: KeyT, value: ValueT) -> None:
        if key in self._cache:
            entry = self._cache[key]
            entry.val = value
            old_key = entry.freq_key()
            entry.touch()
            new_key = entry.freq_key()
            self._update_freq_list(old_key, new_key)
            return

        if len(self._cache) >= self._capacity:
            self._evict_lfu()
        entry = LFUEntry(key=key, val=value)
        self._cache[key] = entry
        self._update_freq_list(old_key=None, new_key=entry.freq_key())

    def print(self):
        print({key: entry.val for key, entry in self._cache.items()})
        for freq in sorted(self._freq_lists):
            freq_list = self._freq_lists[freq]
            if freq_list._head:
                print(f"  freq {freq}: {freq_list}")

    def _update_freq_list(self, old_key, new_key):
        if old_key and old_key[0] in self._freq_lists:
            self._freq_lists[old_key[0]].remove(old_key)
        freq_list = self._freq_lists.get(new_key[0], FreqList())
        freq_list.append(new_key)
        self._freq_lists[new_key[0]] = freq_list

    def _evict_lfu(self):
        if len(self._cache) < self._capacity or len(self._cache) <= 0:
            return
        while len(self._cache) >= self._capacity:
            min_freq = min(self._freq_lists.keys())
            freq_list = self._freq_lists[min_freq]
            if not (freq_list and freq_list._head):
                del self._freq_lists[min_freq]
                continue
            node = freq_list.popleft()
            if not node:
                break
            del self._cache[node.data[2]]
