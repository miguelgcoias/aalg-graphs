import numpy as np

from structs.queue import Queue


def altbfs(graph, source, target=None):
    '''Alternative breadth-first search implementation that takes into account 
    the existence of multiple shortest paths between two vertices.
    
    Keyword arguments:
    graph -- Graph object
    source -- source vertex
    target -- stop searching once target is reached. Default is None, in which 
    case the algorithm runs on the entire graph'''
    inf = np.iinfo(np.int32).max

    # Store distances (levels)
    dist = np.full(graph.order(), inf, dtype='u4')
    dist[source] = 0

    # Number of shortest paths from source to computed vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    # Store parents of computed vertices
    parents = np.empty(graph.order(), dtype='O')

    # Using a queue is not very desirable due to the high number of calls made 
    # to it, but this is the last of all performance related problems we need 
    # to solve
    Q = Queue()
    Q.enqueue(source)
    parents[source] = []

    while not Q.isempty():
        u = Q.dequeue()
        d = dist[u] + 1
        neighbours, _ = graph.neighbours(u)

        for parent in parents[u]:
            sigma[u] += sigma[parent]

        if u == target:
            break

        for neighbour in neighbours:
            if d > dist[neighbour]:
                continue
            elif d < dist[neighbour]:
                dist[neighbour] = d
                parents[neighbour] = [u]
                Q.enqueue(neighbour)
            else:
                parents[neighbour].append(u)
    
    return (dist, parents, sigma)