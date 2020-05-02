import numpy as np
from structs.disjointset import DisjointSet

class GraphStream:
    def __init__(self, path):
        self.path = path
        self.open()

    def __iter__(self):
        return self

    def __next__(self):
        edge = [int(x) for x in self.graph.readline().split()]

        if len(edge) >= 2:
            return edge
        else:
            raise StopIteration
    
    def order(self):
        return self.n

    def size(self):
        return self.m

    # Resets iterators
    def is_connected(self):
        self.open()
        ds = DisjointSet(self.n)

        components = self.n
        for edge in self:
            u, v = edge[:2]
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                components -= 1

        self.close()
        return components == 1

    def open(self):
        self.graph = open(self.path)
        self.n, self.m = [int(x) for x in self.graph.readline().split()]

    def close(self):
        self.graph.close()
