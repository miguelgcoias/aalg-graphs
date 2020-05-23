from array import array
from collections import deque

import numpy as np


def bfs_mpaths(graph, source, target=None):
    '''Alternative breadth-first search implementation that takes into account 
    the existence of multiple shortest paths between two vertices.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    source -- source vertex
    target -- stop searching once target is reached. Default is None, in which 
    case the algorithm runs on the entire graph'''
    # Can this be removed, or done in another way?
    inf = np.iinfo(np.int32).max

    # Store distances (levels)
    dist = [inf for _ in range(graph.order())]
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = [0 for _ in range(graph.order())]
    sigma[source] = 1

    # Store parents of computed vertices
    parents = [None for _ in range(graph.order())]
    parents[source] = []

    # Initialize queue
    Q = deque([source])

    while len(Q) != 0:
        u = Q.pop()
        d = dist[u] + 1
        
        # Avoid function call overhead
        neighbours = graph.adj[graph.ind[u]:graph.ind[u + 1]]

        # Vectorizing this results in worse performance
        for parent in parents[u]:
            sigma[u] += sigma[parent]

        if u == target:
            break

        for neighbour in neighbours:
            if d > dist[neighbour]:
                continue
            elif d < dist[neighbour]:
                dist[neighbour] = d
                parents[neighbour] = [u]
                Q.appendleft(neighbour)
            else:
                parents[neighbour].append(u)
    
    return dist, parents, sigma
