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
    inf = np.iinfo(np.int32).max

    # Store distances (levels)
    dist = array('I', np.full(graph.order(), inf, dtype='u4'))
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = array('I', np.zeros(graph.order(), dtype='u4'))
    sigma[source] = 1

    # Store parents of computed vertices; due to using objects this needs to be 
    # a NumPy array
    parents = np.empty(graph.order(), dtype='O')
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
