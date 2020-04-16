from structs.fpqueue import FPQueue
from structs.graph import Graph


def dijkstra(graph, source):
    # Initialize queue with infinite weights, except for source
    fpq = FPQueue(source, graph.order())

    # Initialize shortest-paths graph
    paths = {v: [[], []] for v in range(graph.order())}

    while not fpq.isempty():
        # Remove from priority queue
        u = fpq.pop()

        # Loop over neighbours of removed root
        vertices, weights = graph.neighbours(u[0])
        for k in range(vertices.size):
            # Avoid neighbours that have already been removed
            if fpq.exists(vertices[k]):
                alt = u[1] + weights[k]
                if alt <= fpq.get(vertices[k])[1]:
                    fpq.update(vertices[k], alt, u[0])
        
        if u[2] is not None:
            paths[u[0]][0] = u[2]
            paths[u[0]][1] = [u[1] for pred in u[2]]
            for pred in u[2]:
                paths[pred][0].append(u[0])
                paths[pred][1].append(u[1])
    
    return paths
