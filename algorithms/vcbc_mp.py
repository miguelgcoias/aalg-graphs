import multiprocessing as mp

import numpy as np
from numpy.random import default_rng

from algorithms.altbfs import altbfs
from algorithms.diam2approx import diam2approx


def vcbc_mp(graph, epsilon, delta):
    '''Assumes graph is connected.'''
    # Diameter 2-approximation, only valid for unweighted graphs
    diam = diam2approx(graph)

    # Number of iterations
    r = np.ceil(0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) - np.log(delta)))

    # To share the bc array between processes, it cannot be a NumPy array (as 
    # far as we know, at least)
    manager = mp.Manager()
    bc = manager.Array('d', np.zeros(graph.order(), dtype='f8'))

    # Execute with multiple processes, while keeping a limit on the number of 
    # running processes at any given time
    with mp.Pool(processes=mp.cpu_count()) as pool:
        for _ in range(np.floor(r/mp.cpu_count()).astype(int)):
            pool.starmap(mpcompute, mp.cpu_count() * [(graph, r, bc)])
        pool.close()
        pool.join()

    return np.array(bc, dtype='f8')

def mpcompute(graph, r, bc):
    rng = default_rng()
    u, v = rng.choice(graph.order(), size=2, replace=False, shuffle=False)
    
    _, preds, sigma = altbfs(graph, u, v)

    t = v
    
    while t != u:
        prob = [sigma[k]/sigma[t] for k in preds[t]]
        z = rng.choice(preds[t], p=prob)
        if z != u:
            bc[z] += r**(-1)
        t = z