import numpy as np
from numpy.random import default_rng

from algorithms.altbfs import altbfs
from algorithms.diam2approx import diam2approx


def vcbc(graph, epsilon, delta):
    '''Assumes graph is connected.'''
    # Store estimated BC scores
    bc = np.zeros(graph.order(), dtype='f8')

    # Diameter 2-approximation, only valid for unweighted graphs
    diam = diam2approx(graph)

    # Number of iterations
    r = np.ceil(0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) - np.log(delta)))

    # Setup random number generator
    rng = default_rng()

    for i in range(r.astype(int)):
        # Random endpoints
        u, v = rng.choice(graph.order(), size=2, replace=False, shuffle=False)
        
        # Run BFS with random endpoints
        _, preds, sigma = altbfs(graph, u, v)

        # Read paper for details
        t = v
        while t != u:
            prob = [sigma[k]/sigma[t] for k in preds[t]]
            z = rng.choice(preds[t], p=prob)
            if z != u:
                bc[z] += 1/r
            t = z
        
    return bc
