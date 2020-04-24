import numpy as np
from numpy.random import default_rng

from algs.dependency import dependency


def mhbc(graph, r, t):
    '''Metropolis-Hastings type algorithm to compute betweenness centrality of 
    vertex v.'''
    # Final distribution
    visits = np.zeros(graph.order(), dtype='u4')

    # New NumPy recommended method for random sampling
    rng = default_rng()

    # Initial state
    v = rng.integers(0, graph.order(), dtype='u4')

    for k in range(t):
        # Proposed next state
        v_new = rng.integers(0, graph.order(), dtype='u4')

        alt = dependency(graph, v_new, r) / dependency(graph, v, r)

        # Probability of transition
        alpha = np.min([1, alt])

        # Accept or reject transition
        u = rng.random()
        if u < alpha:
            v = v_new
        
        # Consider current v as visited
        visits[v] += 1
    
    return visits

