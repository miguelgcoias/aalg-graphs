import numpy as np

class Cuckoo:
    def __init__(self, m, h1, h2):
        self.n = 0
        self.m = m
        self.h1, self.h2 = h1, h2
        self.T = np.empty(m, dtype='O')

        for i in range(m):
            self.T[i] = []

    def search(self, x):
        k1, k2 = self.h1(x), self.h2(x)
        return x == self.T[k1] or x == self.T[k2]

    def insert(self, x):
        k1, k2 = self.h1(x), self.h2(x)
        if x == self.T[k1] or x == self.T[k2]:
            return

        p = k1
        for i in range(n):
            if self.T[p] == None:
                self.T[p] = x
                return

            x = self.T[p]
            k1, k2 = self.h1(x), self.h2(x)

            if p == k1:
                p = k2
            else:
                p = k1

        if self.load_factor() > 0.5:
            self.rehash(self.m * 2)

    def delete(self, x):
        k1, k2 = self.h1(x), self.h2(x)
        if x == self.T[k1]:
            self.T[k1] = None
            self.n -= 1

        if x == self.T[k2]:
            self.T[k2] = None
            self.n -= 1

    def load_factor(self):
        return self.n / self.m
    
    def rehash(self):
        raise NotImplementedError
