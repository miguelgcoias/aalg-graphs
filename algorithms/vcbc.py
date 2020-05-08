import multiprocessing as mp

import numpy as np
from numpy.random import default_rng

from algorithms.bfs_mpaths import bfs_mpaths
from algorithms.diam2approx import diam2approx


def vcbc(graph, epsilon, delta, procs_multiplier=1):
    '''Approximate betweenness centrality of all vertices of graph using the 
    VC-dimension algorithm from 'Fast Approximation of Betweenness Centrality 
    through Sampling' by Kornaropoulos and Riondato. For details, check their 
    paper or our report for a simplified version.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    epsilon -- bound to the quality of the approximation, related to delta
    delta -- bound to the quality of the approximation, related to epsilon
    procs_multiplier -- multiplier on the number of processes to use. Number of 
    processes is given by procs_multiplier * mp.cpu_count()'''
    # Diameter 2-approximation
    diam = diam2approx(graph)

    # Number of iterations
    r = np.ceil(0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) + 1 - np.log(delta)))

    # Execute with multiple processes
    procs = mp.cpu_count() * procs_multiplier
    with mp.Pool(processes=procs) as pool:
        res = pool.starmap(mpcompute, r.astype(int) * [(graph, r)])

    bc = np.sum(res, axis=0)
    return np.array(bc, dtype='f8')


def mpcompute(graph, r):
    # Result for this process
    bc_current = np.zeros(graph.order(), dtype='f8')

    # Randomly select two distinct vertices
    rng = default_rng()
    u, v = rng.choice(graph.order(), size=2, replace=False, shuffle=False)
    _, preds, sigma = bfs_mpaths(graph, u, v)

    t = v
    while t != u:
        prob = [sigma[k]/sigma[t] for k in preds[t]]
        z = rng.choice(preds[t], p=prob)
        if z != u:
            bc_current[z] += r**(-1)
        t = z
    
    return bc_current
