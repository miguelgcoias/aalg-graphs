import numpy as np

from structs.pqueue import PQueue
from structs.digraph import Digraph


def dijkstra(graph, source, target=None):
    '''Standard implementation of Dijkstra's algorithm using a priority queue.
    
    Keyword arguments:
    graph -- WeightedGraph or WeightedDigraph object
    source -- source vertex
    target -- return once target is reached. Default is None, in which case the 
    algorithm runs until the graph has been fully explored)'''
    inf = np.iinfo(np.int32).max

    # Initialize queue with infinite weights, except for source
    PQ = PQueue(source, graph.order())

    # Maintain number of shortest paths from source to all vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    # Store parents of computed vertices
    parents = np.empty(graph.order(), dtype='O')
    parents[source] = []

    # Store distances
    dist = np.full(graph.order(), inf, dtype='f8')
    dist[source] = 0

    while not PQ.isempty():
        # Remove from priority queue
        (v, w, ps) = PQ.pop()
        dist[v] = w

        if ps is not None:
            parents[v] = []
            for p in ps:
                parents[v].append(p)
                sigma[v] += sigma[p]

        # Stop execution when target is found
        if v == target:
            break

        neighbours, weights = graph.neighbours(v)
        for k in range(neighbours.size):
            # Avoid neighbours that have already been removed
            if PQ.exists(neighbours[k]):
                alt = w + weights[k]
                if alt <= PQ.get(neighbours[k])[1]:
                    PQ.update(neighbours[k], alt, v)

    return dist, parents, sigma
