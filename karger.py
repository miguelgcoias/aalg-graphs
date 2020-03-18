import numpy as np
from disjoint_set import DisjointSet
from graph import Graph

def karger(G):
    if not isinstance(G, Graph):
        print("Invalid input")
        return

    num_runs = np.ceil(2 + (G.V * (G.V-1) * np.log2(G.V)) / 2).astype(np.int64)

    min_cut = G.E+1
    for i in range(num_runs):
        min_cut = min(min_cut, contract(G))

    return min_cut

def contract(G):
    edges = G.edges()
    ds = DisjointSet(G.V)
    order = np.random.permutation(G.E)

    edge_idx = 0
    for n in range(G.V-2):
        # Contract graph
        while edge_idx < G.E:
            u, v = edges[order[edge_idx]]
            edge_idx += 1

            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                break

    cut = 0
    for e in edges:
        if ds.find(e[0]) != ds.find(e[1]):
            cut += 1

    return cut

G = Graph('example.json')
print(karger(G))
