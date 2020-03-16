import json
import numpy as np


class Graph:

    def __init__(self, adj):
        self.graph = self.__parse__(adj)

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


# JSON file generated randomly -- not a directed graph!
G = Graph('example.json')
