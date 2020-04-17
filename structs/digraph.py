from json import load

import numpy as np

from structs.graph import Graph


class Digraph(Graph):

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
        return (sums.size, adj.size, adj, ind, weights)

    def __next__(self):
        if self.i < self.n:
            pairs, weights = self.neighbours(self.i)
            if self.j < pairs.size:
                edge = (self.i, pairs[self.j], weights[self.j])
                self.j += 1
                return edge
            else:
                self.i += 1
                self.j = 0
                return self.__next__()
        else:
            raise StopIteration
