import json
import numpy as np


class Digraph:

    def __init__(self, path):
        self.n, self.m, self.adj = self.__parse__(path)

    @staticmethod
    def __parse__(path):
        with open(path) as graph:
            data = json.load(graph)
            n, m = data['n'], data['m']
            adj = np.empty(n, dtype='O')
            for pair in data['adj']:
                adj[pair['v']] = np.array(pair['e'])
        return (n, m, adj)

    def __iter__(self):
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        if self.i < self.n:
            neighbours = self.neighbours(self.i)
            if self.j < neighbours.size:
                edge = (self.i, neighbours[self.j])
                self.j += 1
                return edge
            else:
                self.i += 1
                self.j = 0
                return self.__next__()
        else:
            raise StopIteration

    def neighbours(self, v):
        '''Returns list of outward neighbours of vertex v.'''
        return self.adj[v]

    def order(self):
        '''Return number of vertices.'''
        return self.n

    def size(self):
        '''Return number of edges.'''
        return self.m

    def edges(self):
        return [e for e in self]
