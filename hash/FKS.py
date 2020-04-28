import numpy as np

class FKS:
    def __init__(self, S, m, hash_functions):
        self.m = m
        self.n = len(S)
        self.h = hash_functions
        self.T = np.zeros(m, dtype='O')

        for x in S:
            self.T[hash(x) % self.m] += 1

        for i in range(self.m):
            self.T[i] = np.empty(self.T[i]**2, dtype='O')

        for x in S:
            k = hash(x) % self.m
            self.T[k][self.h[k] % self.m] = x

    def search(self, x):
        k = hash(x) % self.m
        return x == self.T[k][self.h[k] % self.m]

    def insert(self, x):
        raise NotImplementedError

    def delete(self, x):
        raise NotImplementedError

    def load_factor(self):
        return self.n / self.m
