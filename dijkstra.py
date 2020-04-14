from structs.fpqueue import FPQueue
from structs.graph import Graph


def dijkstra(graph, source):
    # Initialize queue with infinite weights, except for source
    fpq = FPQueue(source, graph.order())

    # Initialize shortest-path tree
    spt = {v: [[], []] for v in range(graph.order())}

    while not fpq.isempty():
        # Remove from priority queue
        u = fpq.pop()

        # Loop over neighbours of removed root
        vertices, weights = graph.neighbours(u[0])
        for k in range(vertices.size):
            # The adjacency list of an undirected graph at a vertex may contain
            # a reference to a vertex that has already been deleted from the
            # queue
            try:
                alt = u[1] + weights[k]
                if alt < fpq.get(vertices[k])[1]:
                    fpq.update(vertices[k], alt, u[0])
            except KeyError:
                continue
        
        # Add to shortest-path tree. Perhaps do two directed graphs?
        if u[0] != source:
            spt[u[0]][0].append(u[2])
            spt[u[0]][1].append(u[1])
            spt[u[2]][0].append(u[0])
            spt[u[2]][1].append(u[1])
    
    return spt
