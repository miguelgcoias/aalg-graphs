import numpy as np

from structs.graph import Graph


def floyd_warshall(G, weighted=False):
    infinity = np.iinfo(np.int32).max

    n = G.order()
    dist = np.full((n,n), infinity, dtype=np.int32)

    for edge in G:
        u, v = edge[:2]
        dist[u][v] = edge[2] if weighted else 1

    for v in range(n):
        dist[v][v] = 0

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if dist[v][u] > dist[v][k] + dist[k][u]:
                    dist[v][u] = dist[v][k] + dist[k][u]
    return dist
