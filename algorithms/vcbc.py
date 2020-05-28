import multiprocessing as mp
import random

import numpy as np

from algorithms.bfs_mpaths import bfs_mpaths
from algorithms.diam2approx import diam2approx


def vcbc(graph, epsilon, delta):
    '''Approximate betweenness centrality of all vertices of graph using the 
    VC-dimension algorithm from 'Fast Approximation of Betweenness Centrality 
    through Sampling' by Kornaropoulos and Riondato. For details, check their 
    paper or our report to understand the main ideas.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    epsilon -- bound to the quality of the approximation, related to delta
    delta -- bound to the quality of the approximation, related to epsilon'''
    # Diameter 2-approximation
    diam = diam2approx(graph)

    # Number of iterations
    r = np.ceil(0.5/epsilon**2 * (np.floor(np.log2(diam - 2)) + 1 \
        - np.log(delta))).astype(float)

    # This global hack needs to be done, since mpcompute must inherit this array
    global bc
    bc = mp.Array('d', [0 for _ in range(graph.order())])

    # On Windows platforms, spawning a process will not inherit bc. The way around
    # this is to use multiprocessing.shared_memory, but this is only available on
    # Python 3.8 and PyPy is based on 3.6, so the code isn't going to work with
    # Windows.
    procs = mp.cpu_count()
    with mp.Pool(processes=procs) as pool:
        pool.starmap(mpcompute, int(r) * [(graph, r)])

    # Return as NumPy array?
    return np.array(bc, dtype='f8')


def mpcompute(graph, r):
    # Vertices whose BC score is to be increased by 1/r go here
    chosen = list()
    
    u, v = random.sample(range(graph.order()), 2)
    _, preds, sigma = bfs_mpaths(graph, u, v)

    t = v
    while t != u:
        prob = [sigma[k]/sigma[t] for k in preds[t]]
        # The [0] is necessary because choices always returns a list
        z = random.choices(preds[t], weights=prob)[0]
        if z != u:
            chosen.append(z)
        t = z
    
    with bc.get_lock():
        for v in chosen:
            bc[v] += 1/r
