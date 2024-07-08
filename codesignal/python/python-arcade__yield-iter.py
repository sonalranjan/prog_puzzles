
# https://app.codesignal.com/arcade/python-arcade/yin-and-yang/48HWQ3zKzWJDvHbdF

class Prizes(object):
    def __init__(self, purchases, n, d):
        self._purchases = purchases
        self._n = n
        self._d = d
        self._cnt = n-1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self._cnt < len(self._purchases):
            idx = self._cnt
            self._cnt += self._n
            if self._purchases[idx]%self._d == 0:
                return idx + 1
        raise StopIteration


def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))

