import numpy as np


def bellman_ford(graph, source, weighted=False):
    infinity = np.iinfo(np.int32).max

    n = graph.order()
    dist = np.full(n, infinity, dtype=np.int32)
    pred = np.full(n, infinity, dtype=np.int32)

    dist[source] = 0
    pred[source] = source

    for _ in range(n-1):
        for edge in graph:
            u, v = edge[:2]
            w = edge[2] if weighted else 1
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                pred[u] = v

    for edge in graph:
        u, v = edge[:2]
        w = edge[2] if weighted else 1
        if dist[u] + w < dist[v]:
            raise ValueError("Found negative loop")

        if dist[v] + w < dist[u]:
            raise ValueError("Found negative loop")

    return dist, pred
