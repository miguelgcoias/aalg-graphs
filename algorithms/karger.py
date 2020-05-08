import numpy as np

from structs.disjointset import DisjointSet
from structs.graph import Graph


def karger(G):
    num_runs = np.ceil(2 + (G.order() * (G.order() - 1) * 
    np.log2(G.order())) / 2).astype(np.int64)

    min_cut = G.size() + 1
    for _ in range(num_runs):
        min_cut = min(min_cut, contract(G))

    return min_cut


def contract(G):
    edges = np.array([e for e in G])
    ds = DisjointSet(G.order())
    order = np.random.permutation(G.size())

    edge_idx = 0

    for _ in range(G.order() - 2):
        # Contract graph
        while edge_idx < G.size():
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
