import multiprocessing as mp

import numpy as np
from numpy.random import default_rng

from algorithms.altbfs import altbfs
from algorithms.diam2approx import diam2approx


def vcbc_mp(graph, epsilon, delta, procs_multiplier=1):
    '''Approximate betweenness centrality of all vertices of graph using the 
    VC-dimension algorithm from 'Fast Approximation of Betweenness Centrality 
    through Sampling' by Kornaropoulos and Riondato. For details, check their 
    paper or our report for a simplified version.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    epsilon -- bound to the quality of the approximation, related to delta
    delta -- bound to the quality of the approximation, related to epsilon
    procs_multiplier -- multiplier on the number of processes to use. Number of processes is given by procs_multiplier * mp.cpu_count()'''
    # Diameter 2-approximation
    diam = diam2approx(graph)

    # Number of iterations
    r = 0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) + 1 - np.log(delta))

    # To share the bc array between processes, it cannot be a NumPy array (as 
    # far as we know, at least)
    manager = mp.Manager()
    bc = manager.Array('d', np.zeros(graph.order(), dtype='f8'))

    # Execute with multiple processes
    procs = mp.cpu_count() * 2
    with mp.Pool(processes=procs) as pool:
        for _ in range(np.ceil(r/procs).astype(int)):
            pool.starmap(mpcompute, procs * [(graph, bc, r)])
        pool.close()
        pool.join()

    return np.array(bc, dtype='f8')

def mpcompute(graph, bc, r):
    # Randomly select two distinct vertices
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