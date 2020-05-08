import multiprocessing as mp
from collections import deque

import numpy as np


def brandes(graph, procs_multiplier=1):
    '''Fully parallel implementation of Brandes' algorithm. The main problem is 
    that graph.order() arrays of length graph.order() must be stored in live 
    memory to achieve the best speeds possible; using locks on a shared bc 
    array is very slow since there is a HUGE number of calls to be made in the 
    last lines of mpcompute(). The code is not that great anyway...
    
    Keyword arguments:
    graph -- Graph or Digraph object
    vertex -- vertex to estimate betwenness centrality'''
    # Execute with multiple processes
    procs = mp.cpu_count() * procs_multiplier
    with mp.Pool(processes=procs) as pool:
        res = pool.starmap(mpcompute, [(graph, source) for source in
        range(graph.order())])
    
    bc = np.sum(res, axis=0)
    return np.array(bc, dtype='f8') / (graph.order() * (graph.order() - 1))


def mpcompute(graph, source):
    inf = np.iinfo(np.int32).max

    # Result for this process
    bc_current = np.zeros(graph.order(), dtype='f8')

    # Store dependency scores
    delta = np.zeros(graph.order(), dtype='f8')

    # Store distances (levels)
    dist = np.full(graph.order(), inf, dtype='u4')
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    # Store parents of computed vertices
    parents = np.empty(graph.order(), dtype='O')
    parents[source] = []

    # Initialize stack and queue
    S = deque([])
    Q = deque([source])

    while len(Q) != 0:
        u = Q.pop()
        S.append(u)
        d = dist[u] + 1

        # Avoid function call overhead
        neighbours = graph.adj[graph.ind[u]:graph.ind[u+1]]

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
            bc_current[v] += delta[v]
    
    return bc_current
