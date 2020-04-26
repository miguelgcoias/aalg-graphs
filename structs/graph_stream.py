import numpy as np

class GraphStream:
    def __init__(self, path):
        self.graph = open(path)

    def __iter__(self):
        self.n = int(self.graph.readline())
        return self

    def __next__(self):
        edge = self.graph.readline().split()

        if len(edge) >= 2:
            return edge
        else:
            raise StopIteration
    
    def order(self):
        ''' Return number of vertices '''
        return self.n
