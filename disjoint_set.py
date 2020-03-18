import numpy as np

class DisjointSet:
    def __init__(self, N):
        self.N = N
        self.par = np.empty(N, dtype=np.int64)
        self.size  = np.ones(N, dtype=np.int64)

        for i in range(N):
            self.par[i] = i

    def find(self, a):
        if a == self.par[a]:
            return a

        self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if(a == b):
            return

        if(self.size[a] > self.size[b]):
            a, b = b, a

        self.size[b] += self.size[a]
        self.par[a] = b
