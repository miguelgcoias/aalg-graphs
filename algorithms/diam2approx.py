import numpy as np
from numpy.random import default_rng

from algorithms.alternative_bfs import alternative_bfs


def diam2approx(graph):
    # Random source vertex
    rng = default_rng()
    v = rng.integers(0, graph.order(), dtype='u4')

    # Run BFS for a random vertex, and subtract 1 from depth array to obtain 
    # length of path
    dist = alternative_bfs(graph, v)[0] - 1

    # Maximum distance
    highest = np.amax(dist)

    if len(np.where(dist == highest)[0]) > 1:
        # Two largest shortest paths with same length
        return highest * 2
    else:
        # Maximum multiplied by second highest value
        return highest + np.amax((dist != np.amax(dist)) * dist)