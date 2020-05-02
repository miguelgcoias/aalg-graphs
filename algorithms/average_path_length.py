import math
import numpy as np
from algorithms.BFS import BFS
from algorithms.bellman_ford import bellman_ford

def average_path_length(graph, algorithm='BFS'):
    n = graph.order()

    ret = 0
    if algorithm == 'Flajolet_Martin':
        ret = approximate_distance_sum(graph)
        
    for v in range(n):
        if algorithm == 'Bellman_Ford':
            dist, _ = bellman_ford(graph, v)
        else: # algorithm == 'BFS'
            dist, _, _ = BFS(graph, v)
            # TODO find infinite

        for u in range(v+1, n):
            ret += dist[u]
    ret *= 2
    ret /= n * (n-1)

    return ret

def approximate_distance_sum(graph, hash_functions):
    n = graph.order()
    k = len(hash_functions)
    m = np.int64(2 ** 32)
    max_zeros = 32

    r = np.zeros((n, k), dtype=np.int64)
    neighbours = np.zeros(n, dtype=np.int64)

    for edge in graph:
        u, v = edge[:2]
        for idx, h in enumerate(hash_functions):
            r[u][idx] = max(r[u][idx], tail_length(h(v, m), max_zeros))
            r[v][idx] = max(r[v][idx], tail_length(h(u, m), max_zeros))

    for u in range(n):
        tmp = np.double(0)
        for idx in range(k):
            tmp += r[u][idx]
        tmp /= k

        neighbours[u] = 2 ** tmp
    return neighbours

def tail_length(x, m):
    if x == 0:
        return m

    n = np.int64(0)
    while x % 2 ** (n+1) == 0:
        n += 1
    return n
