import numpy as np

def BFS(graph, source):
    infinity = np.iinfo(np.int32).max

    n = graph.order()
    dist = np.full(n, infinity, dtype=np.int32)
    pred = np.empty(n, dtype=np.int32)
    order = np.empty(n, dtype=np.int32)

    dist[source] = 0
    pred[source] = source

    order[0] = source
    order[n-1] = -1

    waiting_beginning = 0
    waiting_end = 0

    while waiting_beginning <= waiting_end:
        v = order[waiting_beginning]
        neighbours = graph.neighbours(v)[0]

        for u in neighbours:
            if dist[u] == infinity:
                dist[u] = dist[v] + 1
                waiting_end += 1
                order[waiting_end] = u
                pred[u] = v

        waiting_beginning += 1

    return dist, pred, order
