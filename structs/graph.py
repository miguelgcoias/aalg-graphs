from json import load
import numpy as np


class Graph:

    def __init__(self, path):
        self.n, self.m, self.adj, self.ind, self.wts = self.__parse(path)

    @staticmethod
    def __parse(path):
        with open(path) as graph:
            # Code quality and performance can likely be improved. Only supports up to 2**32 - 1 vertices, due to using 32-bit unsigned integers. Should this be changed?
            graph = load(graph)
            adj = np.array([v for adj in graph.values() for v in adj[0]], dtype='u4')
            wts = np.array([w for adj in graph.values() for w in adj[1]], dtype='f8')
            lensums = np.cumsum(np.array([len(adj[0]) for adj in graph.values()]), dtype='u4')
            ind = np.concatenate((np.array([0], dtype='u4'), lensums))
        # Check if methods like Boruvka or Karger-Stein expect the true number of edges or the internal representation adj.size. For now, returns the true number
        return (lensums.size, int(adj.size/2), adj, ind, wts)
    
    def __iter__(self):
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        # To do: something about weights, read line 52
        if self.i < self.n:
            pairs, weights = self.neighbours(self.i)
            if self.j < pairs.size:
                # To do: the check below must not be present in Digraph, else the iterator will not return all edges
                if self.i <= pairs[self.j]:
                    edge = (self.i, pairs[self.j], weights[self.j])
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
        '''Returns array of neighbours of vertex v.
        Expect this function to return garbage if v < 0.'''
        return (self.adj[self.ind[v]:self.ind[v + 1]], self.wts[self.ind[v]:self.ind[v + 1]])
    
    def weights(self, adj):
        # Including edge weights on the iterator will break functionality, and if the result from the iterator is stored as a NumPy array, all indices become floating point. This further breaks functionality.
        return NotImplementedError

    def order(self):
        '''Return number of vertices.'''
        return self.n

    def size(self):
        '''Return number of edges.'''
        # Check comment in line 19
        return self.m
