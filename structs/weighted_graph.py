from array import array
from json import load

from structs.graph import Graph


class WeightedGraph(Graph):

    def __init__(self, data):
        '''Static sparse weighted graph class constructor. Allows reading from 
        a JSON file or from a dictionary object mimicking the structure of a 
        loaded JSON file.
        
        Keyword arguments:
        data -- path to JSON file, or dictionary object as described above'''
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
            raise TypeError('Invalid input')


    @staticmethod
    def _parse(graph):
        # Implicitly relies on the dict ordering to work
        adj = array('I', [v for adj in graph.values() for v in adj])
        weights = array('d', [w for adj in graph.values() for w in adj[1]])
        ind = array('I', [0])
        ind.extend([len(adj) for adj in graph.values()])
        for i in range(1, len(ind)):
            ind[i] += ind[i - 1]
        return len(ind) - 1, len(adj), adj, ind, weights
    
    def __iter__(self):
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        if self.i < self.n:
            pairs, weights = self.neighbours(self.i)
            if self.j < len(pairs):
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
        '''Returns array of neighbours of v and their weights.
        
        Keyword arguments:
        v -- vertex to find neighbours of'''
        inds = slice(self.ind[v], self.ind[v + 1])
        return self.adj[inds], self.weights[inds]
