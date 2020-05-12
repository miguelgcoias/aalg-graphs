import numpy as np
from numpy.random import default_rng

from algorithms.bfs_mpaths import bfs_mpaths


def diam2approx(graph):
    '''Find 2-approximation of diameter of graph.
    
    Keyword arguments:
    graph -- Graph or Digraph object'''
    # Random source vertex
    rng = default_rng()
    v = rng.integers(0, graph.order(), dtype='u4')

    # Run BFS for a random vertex, and subtract 1 from depth array to obtain 
    # length of path
    dist, _, _ = bfs_mpaths(graph, v)
    dist = np.array(dist)

    # Maximum distance
    highest = np.amax(dist)

    if len(np.where(dist == highest)[0]) > 1:
        # Two largest shortest paths with same length
        return highest * 2
    else:
        # Maximum multiplied by second highest value
        return highest + np.amax(dist[dist != np.amax(dist)])
