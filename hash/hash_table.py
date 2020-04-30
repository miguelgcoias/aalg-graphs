import numpy as np

class HashTable:
    def __init__(self, m=1):
        self.n = 0
        self.m = m
        self.T = np.empty(m, dtype='O')

        for i in range(m):
            self.T[i] = []

    def search(self, x):
        return x in self.T[hash(x) % self.m]

    def insert(self, x):
        self.T[hash(x) % self.m].append(x)
        self.n += 1

        if(self.load_factor() > 0.5):
            self.rehash(self.m * 2)

    def delete(self, x):
        self.T[hash(x) % self.m].remove(x)
        self.n -= 1

    def load_factor(self):
        return self.n / self.m
    
    def rehash(self):
        raise NotImplementedError
