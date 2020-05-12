import multiprocessing as mp

import numpy as np
from numpy.random import default_rng

from algorithms.bfs_mpaths import bfs_mpaths
from algorithms.diam2approx import diam2approx


def vcbc(graph, epsilon, delta):
    '''Approximate betweenness centrality of all vertices of graph using the 
    VC-dimension algorithm from 'Fast Approximation of Betweenness Centrality 
    through Sampling' by Kornaropoulos and Riondato. For details, check their 
    paper or our report for a simplified version.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    epsilon -- bound to the quality of the approximation, related to delta
    delta -- bound to the quality of the approximation, related to epsilon'''
    # Diameter 2-approximation
    diam = diam2approx(graph)

    # Number of iterations
    r = np.ceil(0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) + 1 \
        - np.log(delta)))

    # pylint shows a ficticious error on line 32
    # Check https://github.com/PyCQA/pylint/issues/3313
    manager = mp.Manager()
    bc = manager.Array('d', np.zeros(graph.order(), dtype='f8'))
    lock = manager.Lock()

    # Execute with multiple processes
    procs = mp.cpu_count()
    with mp.Pool(processes=procs) as pool:
        pool.starmap(mpcompute, r.astype(int) * [(graph, bc, lock, r)])

    return np.array(bc, dtype='f8')


def mpcompute(graph, bc, lock, r):
    # Chosen vertices
    chosen = list()
    
    # Randomly select two distinct vertices
    rng = default_rng()
    u, v = rng.choice(graph.order(), size=2, replace=False, shuffle=False)
    _, preds, sigma = bfs_mpaths(graph, u, v)

    t = v
    while t != u:
        prob = [sigma[k]/sigma[t] for k in preds[t]]
        z = rng.choice(preds[t], p=prob)
        if z != u:
            chosen.append(z)
        t = z
    
    with lock:
        for v in chosen:
            bc[v] += r**(-1)
