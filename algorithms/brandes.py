import multiprocessing as mp
from collections import deque

import numpy as np


def brandes(graph):
    '''Fully parallel implementation of Brandes' algorithm. The main problem is 
    that graph.order() arrays of length graph.order() must be stored in live 
    memory to achieve the best speeds possible; using locks on a shared bc 
    array is very slow since there is a HUGE number of calls to be made in the 
    last lines of mpcompute(). The code is not that great anyway...
    
    Keyword arguments:
    graph -- Graph or Digraph object
    vertex -- vertex to estimate betwenness centrality'''
    # This global hack is ugly, but it needs to be done since mpcompute must
    # be able to modify this array
    global bc
    bc = mp.Array('d', [0 for _ in range(graph.order())])

    procs = mp.cpu_count()
    with mp.Pool(processes=procs) as pool:
        pool.starmap(mpcompute, [(graph, src) for src in range(graph.order())])
    
    return np.array(bc, dtype='f8') / (graph.order() * (graph.order() - 1))


def mpcompute(graph, source):
    inf = np.iinfo(np.int32).max

    # Store dependency scores
    delta = [0 for _ in range(graph.order())]

    # Store distances (levels)
    dist = [inf for _ in range(graph.order())]
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = [0 for _ in range(graph.order())]
    sigma[source] = 1

    # Store parents of computed vertices
    parents = [None for _ in range(graph.order())]
    parents[source] = []

    # Initialize queue and stack
    Q = deque([source])
    S = deque([])

    while len(Q) != 0:
        u = Q.pop()
        S.append(u)
        d = dist[u] + 1

        # Avoid function call overhead
        neighbours = graph.adj[graph.ind[u]:graph.ind[u + 1]]

        # Vectorizing this results in worse performance
        for parent in parents[u]:
            sigma[u] += sigma[parent]

        for neighbour in neighbours:
            if d > dist[neighbour]:
                continue
            elif d < dist[neighbour]:
                dist[neighbour] = d
                parents[neighbour] = [u]
                Q.appendleft(neighbour)
            else:
                parents[neighbour].append(u)
    
    while len(S) != 0:
        v = S.pop()
        for p in parents[v]:
            delta[p] += sigma[p] / sigma[v] * (1 + delta[v])
        if v != source:
            # This is not a very good idea. We don't care since we just want a
            # correct version of Brandes which performs reasonably well
            with bc.get_lock():
                bc[v] += delta[v]
