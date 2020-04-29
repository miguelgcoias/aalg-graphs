import numpy as np
from numpy.random import default_rng

from algs.dependency import dependency


def mhbc(graph, r, t):
    '''Metropolis-Hastings type algorithm to compute betweenness centrality of 
    vertex r.'''
    # Betweenness centrality of r
    cb = 0

    # New NumPy recommended method for random sampling
    rng = default_rng()

    # Initial state
    v = rng.integers(0, graph.order(), dtype='u4')

    # v cannot be equal to r
    while v == r:
        v = rng.integers(0, graph.order(), dtype='u4')

    # Dependency of r on v
    delta_v = dependency(graph, v, r)

    for k in range(t):
        # Proposed next state
        w = rng.integers(0, graph.order(), dtype='u4')

        # w cannot be equal to r
        while w == r:
            w = rng.integers(0, graph.order(), dtype='u4')
        
        # Dependency of r on w (proposed next state)
        delta_w = dependency(graph, w, r)

        # Probability of transition
        alpha = np.min([1, delta_w / delta_v])

        # Pick a random number between 0 and 1
        mu = rng.random()

        # Accept or reject transition
        if mu < alpha:
            v = w
            delta_v = delta_w
            cb += delta_v
    
    # Be careful with overflow here...
    cb /= ((t + 1) * (graph.order() - 1))
    
    return cb
