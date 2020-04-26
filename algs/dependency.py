import numpy as np

from structs.pqueue import PQueue
from structs.stack import Stack


def dependency(graph, s, v):
    '''Partial implementation of Brandes' algorithm. Does not compute the 
    betweenness centrality, since that would involve iterating over all 
    vertices of the graph -- this partial version does one iteration of 
    Brandes' algorithm.'''
    # Initialize queue with infinite weights, except for source
    PQ = PQueue(s, graph.order())

    # Initialize stack
    S = Stack()

    # Maintain number of shortest paths from source to all vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[s] = 1

    # Dependency scores
    delta = np.zeros(graph.order(), dtype='f8')

    # Dijkstra's algorithm
    while not PQ.isempty():
        # Remove from priority queue
        (vertex, weight, preds) = PQ.pop()

        # Add to stack
        S.push((vertex, preds))

        if preds is not None:
            for pred in preds:
                # Combinatorial path counting lemma
                sigma[vertex] += sigma[pred]

        neighbours, weights = graph.neighbours(vertex)
        for k in range(neighbours.size):
            # Avoid neighbours that have already been removed
            if PQ.exists(neighbours[k]):
                alt = weight + weights[k]
                if alt <= PQ.get(neighbours[k])[1]:
                    PQ.update(neighbours[k], alt, vertex)

    while not S.isempty():
        # Remove from stack
        (vertex, preds) = S.pop()

        if preds is not None:
            for pred in preds:
                delta[pred] += sigma[pred] / sigma[vertex] * (1 + delta[vertex])
    
    return delta[v]
