import math

import numpy as np

from algorithms.bellman_ford import bellman_ford
from algorithms.bfs import bfs


def average_path_length(graph, algorithm='bfs'):
    n = graph.order()

    ret = 0
    for v in range(n):
        if algorithm == 'Bellman_Ford':
            dist, _ = bellman_ford(graph, v)
        else: # algorithm == 'bfs'
            dist, _, _ = bfs(graph, v)
            # TODO find infinite

        for u in range(v+1, n):
            ret += dist[u]
    ret *= 2
    ret /= n * (n-1)

    return ret
