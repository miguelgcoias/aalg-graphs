from json import load

import numpy as np

from structs.graph import Graph


class Digraph(Graph):

    def __init__(self, data):
        '''Static sparse digraph class constructor. Allows reading from a JSON 
        file or from a dictionary object mimicking the structure of a loaded 
        JSON file.
        
        Keyword arguments:
        data -- path to JSON file, or dictionary object as described above'''
        if isinstance(data, str):
            with open(data) as graph_json:
                graph = load(graph_json)
                self.n, self.m, self.adj, self.ind, self.weights = \
                    super()._parse(graph)
        elif isinstance(data, dict):
            self.n, self.m, self.adj, self.ind, self.weights = \
                super()._parse(data)
        else:
            raise RuntimeError('Invalid input')

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
