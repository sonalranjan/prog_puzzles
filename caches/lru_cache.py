from base import KeyT, LRUCacheBase, ValueT


class LNode:

    def __init__(self, k: KeyT = None, v: ValueT = None):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

    def __repr__(self):
        s = ''
        if self.prev:
            s += f' {self.prev.key} <-- '
        s += f'k={self.key} v={self.val}'
        if self.next:
            s += f' --> {self.next.key}'
        return f'[{s}]'


class LRUCache(LRUCacheBase):

    def __init__(self, capacity=100):
        self._cache = {}
        self._capacity = capacity

        # ordering
        self._head = LNode(k="__head", v=None)
        self._tail = LNode(k="__tail", v=None)
        self._tail.prev = self._head
        self._head.next = self._tail

    def get(self, k: KeyT) -> ValueT:
        if k not in self._cache:
            return None
        node = self._cache[k]
        node = self._remove(node)
        node = self._insertFront(node)
        self._cache[k] = node
        return node

    def put(self, k: KeyT, v: ValueT):
        while len(self._cache) > self._capacity:
            print(self._cache)
            if self._tail.prev != self._head:
                node = self._remove(self._tail.prev)
                del self._cache[node._key]

        node = LNode(k, v)
        node = self._insertFront(node)
        self._cache[k] = node

    def _insertFront(self, node):
        node.prev = self._head
        node.next = self._head.next
        if node.next:
            node.next.prev = node
        self._head.next = node
        return node

    def _remove(self, node):
        if not node:
            return node

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.prev, node.next = None, None
        return node

    def print(self):
        s = ''
        node = self._head
        while node:
            s += str(node)
            node = node.next
        print(s)
