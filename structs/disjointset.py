import numpy as np

class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.par = np.arange(n, dtype=np.int64)
        self.size = np.ones(n, dtype=np.int64)

    def find(self, a):
        if a == self.par[a]:
            return a

        self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        if self.size[a] > self.size[b]:
            a, b = b, a

        self.size[b] += self.size[a]
        self.par[a] = b
