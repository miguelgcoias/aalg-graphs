import numpy as np
from structs.graph import Graph

def bellman_ford(G, source, weighted=False):
    infinity = np.iinfo(np.int32).max

    n = G.order()
    dist = np.full(n, infinity, dtype=np.int32)
    pred = np.full(n, infinity, dtype=np.int32)

    dist[source] = 0
    pred[source] = source

    for i in range(n-1):
        for edge in G:
            u, v = edge[:2]
            w = edge[2] if weighted else 1
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

    for edge in G:
        u, v = edge[:2]
        w = edge[2] if weighted else 1
        if dist[u] + w < dist[v]:
            raise ValueError("Found negative loop")

    return dist, pred
