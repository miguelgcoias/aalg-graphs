from json import load
import numpy as np

class Graph:

    def __init__(self, path):
        self.n, self.m, self.adj, self.ind = self.__parse(path)

    @staticmethod
    def __parse(path):
        with open(path) as graph:
            # Code quality and performance can likely be improved
            graph = load(graph)
            adj = np.array([v for adj in graph.values() for v in adj], dtype='u4')
            length_sums = np.cumsum(np.array([len(adj) for adj in graph.values()]), dtype='u4')
            # Use np.concatenate() instead?
            ind = np.zeros(length_sums.size + 1, dtype='u4')
            ind[1:] = length_sums
        return (length_sums.size, adj.size, adj, ind)
    
    def __iter__(self):
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        if self.i < self.n:
            pairs = self.neighbours(self.i)
            if self.j < pairs.size:
                if self.i <= pairs[self.j]:
                    edge = (self.i, pairs[self.j])
                    self.j += 1
                    return edge
                else:
                    self.j += 1
                    return self.__next__()
            else:
                self.i += 1
                self.j = 0
                return self.__next__()
        else:
            raise StopIteration
    
    def neighbours(self, v):
        '''Returns array of neighbours of vertex v.'''
        return self.adj[self.ind[v]:self.ind[v + 1]]

    def order(self):
        '''Return number of vertices.'''
        return self.n

    def size(self):
        '''Return number of edges.'''
        # Should this return m/2?
        return self.m
