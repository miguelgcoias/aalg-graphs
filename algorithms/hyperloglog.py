import numpy as np


def leading_zeros(x, left=32, right=0):
    for i in range(left, right, -1):
        if x & 2 ** i != 0:
            return (left-i) + 1

    return (left-right) + 1


class HyperLogLogCounter:
    def __init__(self, b):
        self.b = b
        self.p = 2 ** b
        self.counter = np.zeros(self.p, dtype=np.uint8)

    def size(self):
        ret = 0
        for j in range(self.p):
            ret += 2 ** (-self.counter[j])

        ret = self.alpha * self.p**2 / ret
        return ret

    def add(self, x):
        pass

    def union(self, other):
        pass
