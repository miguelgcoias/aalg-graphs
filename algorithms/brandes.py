import multiprocessing as mp
# from multiprocessing.sharedctypes import RawArray

import numpy as np

from structs.queue import Queue
from structs.stack import Stack


def brandes(graph, procs_multiplier=1):
    '''Standard implementation of Brandes' algorithm.
    
    Keyword arguments:
    graph -- Graph or Digraph object
    vertex -- vertex to estimate betwenness centrality'''

    # Betweenness centrality scores
    # bc = np.zeros(graph.order(), dtype='f8')

    # Share bc array between processes
    manager = mp.Manager()
    # If your venv has pylint, the following line may present a ficticious 
    # problem. Read https://github.com/PyCQA/pylint/issues/3313
    lock = manager.Lock()
    bc = manager.Array('d', np.zeros(graph.order(), dtype='f8'))

    procs = mp.cpu_count() * procs_multiplier

    with mp.Pool(processes=procs) as pool:
        pool.starmap(mpcompute, [(bc, lock, graph, source) for source in
        range(graph.order())])
    
    return np.array(bc, dtype='f8') / (graph.order() * (graph.order() - 1))

def mpcompute(bc, lock, graph, source):
    inf = np.iinfo(np.int32).max

    # Initialize stack
    S = Stack()

    # Store distances (levels)
    dist = np.full(graph.order(), inf, dtype='u4')
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    # Store parents of computed vertices
    parents = np.empty(graph.order(), dtype='O')
    parents[source] = []

    # Using a queue is not very desirable due to the high number of calls 
    # needed, but this is the last of all performance problems we need to solve
    Q = Queue()
    Q.enqueue(source)

    while not Q.isempty():
        u = Q.dequeue()
        S.push(u)
        d = dist[u] + 1
        neighbours = graph.neighbours(u)

        # Vectorizing this results in worse performance
        for parent in parents[u]:
            sigma[u] += sigma[parent]

        for neighbour in neighbours:
            if d > dist[neighbour]:
                continue
            elif d < dist[neighbour]:
                dist[neighbour] = d
                parents[neighbour] = [u]
                Q.enqueue(neighbour)
            else:
                parents[neighbour].append(u)
    
    # Store dependency scores
    delta = np.zeros(graph.order(), dtype='f8')
    
    while not S.isempty():
        v = S.pop()
        for p in parents[v]:
            delta[p] += sigma[p] / sigma[v] * (1 + delta[v])
        if v != source:
            # Terrible performance...
            with lock:
                bc[v] += delta[v]

