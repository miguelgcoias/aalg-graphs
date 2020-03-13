import numpy as np


class Vertex:

    def __init__(self, v):
        self.v = v
    
    def __eq__(self, E):
        return self.v == E.name()
    
    def __hash__(self):
        return hash(self.v)

    def name(self):
        return self.v


class Edge:

    def __init__(self, v, w):
        self.v = v
        self.w = w

    def __eq__(self, E):
        return self.v == E.start() and self.w == E.end()
    
    def __hash__(self):
        return hash((self.v, self.w))
    
    def start(self):
        return self.v

    def end(self):
        return self.w
    
    def reverse(self):
        self.v, self.w = self.w, self.v


class Graph:

    # dir: whether the graph is directed or not. For now, does nothing
    def __init__(self, V, E, dir=True):
        self.G = dict.fromkeys([Vertex(v) for v in V], None)
        self.dir = dir

        for v in E:
            self.G[Vertex(v)] = [Edge(Vertex(v), Vertex(w)) for w in E[v]]
    
    def vertices(self):
        return np.array([v for v in self.G.keys()])
    
    def edges(self):
        # Not very good code, redo later
        edge_list = self.G.copy()

        for v in self.G:
            if edge_list[v] is None:
                edge_list.pop(v)
        
        return edge_list
        
    def neighbours(self, v):
        pass

    def contract(self, v, w):
        pass

V = ['A', 'B', 'C', 'D', 'E']
E = {'A':['B', 'C'], 'B':['C'], 'C':['D'], 'D':['E']}
G = Graph(V, E)
print(G.edges())
