import numpy as np


class Vertex:

    def __init__(self, v):
        self.v = v

class Edge:

    def __init__(self, v, w):
        self.v = v
        self.w = w
    
    def start(self):
        return self.v

    def end(self):
        return self.w
    
    def merge(self, E):
        if self.w == E.start():
            return Edge(self.v, E.end())
        elif self.v == E.end():
            return Edge(E.start(), self.w)
        else:
            pass

class Graph:

    def __init__(self, V, E):
        self.V = np.array([Vertex(v) for v in V])
        self.E = dict()

        for e in E:
            self.E[Vertex(e[0])] = np.array([Edge(Vertex(e[0]), Vertex(v))
            for v in e[1:]])
        
    def neighbours(self, v):
        return self.E[v]

    def contract(self, nodes):
        pass


# V = np.array(['A', 'B', 'C', 'D', 'E'])
# E = np.array([['A', 'B', 'C'], ['B', 'C'], ['C', 'D'], ['D', 'E']])
# G = Graph(V, E)
