from base import KeyT, LRUCacheBase, ValueT

# https://leetcode.com/problems/lfu-cache/


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 0
        self.order = 0
        self.prev = None
        self.next = None


class FreqList:

    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, node):
        if not self._head:
            self._head = node
            self._tail = node
            return
        self._tail.next = node
        node.prev = self._tail
        self._tail = node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        if prev:
            prev.next = nxt
        else:
            self._head = nxt
        if nxt:
            nxt.prev = prev
        else:
            self._tail = prev
        node.prev = None
        node.next = None

    def popleft(self):
        if not self._head:
            return None
        node = self._head
        self.remove(node)
        return node

    def __bool__(self):
        return self._head is not None


class LFUCache(LRUCacheBase):

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._freq_lists = {}
        self._min_freq = 0
        self._counter = 0

    def get(self, key: KeyT) -> ValueT | None:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._bump(node)
        return node.val

    def put(self, key: KeyT, value: ValueT) -> None:
        if self._capacity <= 0:
            return

        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._bump(node)
            return

        if len(self._cache) >= self._capacity:
            self._evict()

        node = Node(key, value)
        node.freq = 1
        self._counter += 1
        node.order = self._counter
        self._cache[key] = node
        self._add_to_freq_list(node)
        self._min_freq = 1

    def print(self):
        print({key: node.val for key, node in self._cache.items()})
        for freq in sorted(self._freq_lists):
            freq_list = self._freq_lists[freq]
            if not freq_list:
                continue
            keys = []
            node = freq_list._head
            while node:
                keys.append(node.key)
                node = node.next
            print(f"  freq {freq}: {keys}")

    def _freq_list(self, freq):
        if freq not in self._freq_lists:
            self._freq_lists[freq] = FreqList()
        return self._freq_lists[freq]

    def _add_to_freq_list(self, node):
        self._freq_list(node.freq).append(node)

    def _remove_from_freq_list(self, node):
        freq = node.freq
        self._freq_lists[freq].remove(node)
        if not self._freq_lists[freq]:
            del self._freq_lists[freq]
            if freq == self._min_freq:
                self._min_freq += 1

    def _bump(self, node):
        self._remove_from_freq_list(node)
        node.freq += 1
        self._counter += 1
        node.order = self._counter
        self._add_to_freq_list(node)

    def _evict(self):
        freq_list = self._freq_lists[self._min_freq]
        node = freq_list.popleft()
        del self._cache[node.key]
        if not freq_list:
            del self._freq_lists[self._min_freq]
