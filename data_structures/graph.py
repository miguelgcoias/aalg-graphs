import json
import numpy as np

class Graph:
    def __init__(self, adj):
        self.graph = self.__parse__(adj)
        self.V = len(self.graph)

        self.E = 0
        for v in range(self.V):
            self.E += len(self.graph[v])
        self.E /= 2

    @staticmethod
    def __parse__(adj):
        with open(adj) as graph:
            data = json.load(graph)
            adj = np.empty(data['n'], dtype='O')
            for pair in data['adj']:
                adj[pair['v']] = np.array(pair['e'])

        return adj
    
    def neighbours(self, v):
        return self.graph[v]

    # Return number of vertices 
    def order(self):
        return self.V

    # Return number of edges
    def size(self):
        return self.E

    def edges_iterator(self):
        for v in range(self.V):
            for u in self.graph[v]:
                if v < u:
                    yield (v, u)

    def edges(self):
        itr = self.edges_iterator()
        return [next(itr) for e in range(self.E)]
