from json import load

import numpy as np


class Graph:

    def __init__(self, data, fromobject=False):
        if not fromobject:
            with open(data) as graphjson:
                graph = load(graphjson)
                self.n, self.m, self.adj, self.ind, self.weights = \
                    self._parse(graph)
        else:
            self.n, self.m, self.adj, self.ind, self.weights = self._parse(data)

    @staticmethod
    def _parse(graph):
        # Code quality and performance can likely be improved
        adj = np.array([v for adj in graph.values() for v in adj[0]],
        dtype='i4')
        weights = np.array([w for adj in graph.values() for w in adj[1]],
        dtype='f8')
        sums = np.cumsum(np.array([len(adj[0]) for adj in graph.values()]), 
        dtype='i4')
        ind = np.concatenate((np.array([0], dtype='i4'), sums))
        # Check if methods like Boruvka or Karger-Stein expect the true number
        # of edges or the internal representation adj.size. For now, returns
        # the true number
        return (sums.size, int(adj.size/2), adj, ind, weights)
    
    def __iter__(self):
        '''Iterating over a graph returns its edges 'partially' ordered, that
        is, (v, s) will be returned before (v+1, t) independently of how s
        compares to t, but we don't order the endpoints. To avoid repeats,
        edges returned are in the format (v, w) where v <= w'''
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        if self.i < self.n:
            pairs, weights = self.neighbours(self.i)
            if self.j < pairs.size:
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
        return (self.adj[self.ind[v]:self.ind[v + 1]],
            self.weights[self.ind[v]:self.ind[v + 1]])

    def order(self):
        '''Return number of vertices.'''
        return self.n

    def size(self):
        '''Return number of edges.'''
        # Check comment on lines 22-24
        return self.m
