from json import load

import numpy as np


class Graph:

    def __init__(self, data):
        '''Static sparse graph class constructor. Allows reading from a JSON 
        file or from a dictionary object mimicking the structure of a loaded 
        JSON file.
        
        Keyword arguments:
        data -- path to JSON file, or dictionary object as described above'''
        try:
            if isinstance(data, str):
                with open(data) as graph_json:
                    graph = load(graph_json)
                    self.n, self.m, self.adj, self.ind, self.weights = \
                        self._parse(graph)
                    self.m = int(self.m/2)
            elif isinstance(data, dict):
                self.n, self.m, self.adj, self.ind, self.weights = \
                    self._parse(data)
                self.m = int(self.m/2)
            else:
                raise RuntimeError('Invalid input')
        except RuntimeError:
            raise


    @staticmethod
    def _parse(graph):
        # Performance can likely be improved. Do further testing
        adj = np.array([v for adj in graph.values() for v in adj[0]],
        dtype='u4')
        weights = np.array([w for adj in graph.values() for w in adj[1]],
        dtype='f8')
        sums = np.cumsum(np.array([len(adj[0]) for adj in graph.values()]), 
        dtype='u4')
        ind = np.concatenate((np.array([0], dtype='u4'), sums))
        return (sums.size, adj.size, adj, ind, weights)
    
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
        inds = slice(self.ind[v], self.ind[v+1])
        return (self.adj[inds], self.weights[inds])

    def order(self):
        '''Return number of vertices.'''
        return self.n

    def size(self):
        '''Return number of edges.'''
        # Check comment on lines 22-24
        return self.m
