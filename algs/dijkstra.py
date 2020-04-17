import numpy as np

from structs.fpqueue import FPQueue
from structs.digraph import Digraph


def dijkstra(graph, source):
    # Initialize queue with infinite weights, except for source
    fpq = FPQueue(source, graph.order())

    # Initialize shortest-paths digraphs
    outpaths = {v: [[], []] for v in range(graph.order())}
    inpaths = {v: [[], []] for v in range(graph.order())}

    # Maintain number of shortest paths from source to all vertices
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    while not fpq.isempty():
        # Remove from priority queue
        u = fpq.pop()

        # Loop over neighbours of removed root
        vertices, weights = graph.neighbours(u[0])
        for k in range(vertices.size):
            # Avoid neighbours that have already been removed
            if fpq.exists(vertices[k]):
                alt = u[1] + weights[k]
                # Equality matters
                if alt <= fpq.get(vertices[k])[1]:
                    fpq.update(vertices[k], alt, u[0])
        
        # Generate outward and inward flowing directed graphs with 
        # shortest-paths
        # Check if this is really necessary -- outward flow must be kept
        if u[2] is not None:
            for pred in u[2]:
                outpaths[pred][0].append(u[0])
                outpaths[pred][1].append(u[1])
                inpaths[u[0]][0].append(pred)
                inpaths[u[0]][1].append(u[1])
                # Combinatorial path counting lemma
                sigma[u[0]] += sigma[pred]
        
    outpaths = Digraph(outpaths, fromobject=True)
    inpaths = Digraph(inpaths, fromobject=True)
    
    return (outpaths, inpaths, sigma)
