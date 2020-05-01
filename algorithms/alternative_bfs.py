import numpy as np

from structs.queue import Queue


def alternative_bfs(graph, source, target=None):
    Q = Queue()

    # Mark vertices as visited
    visits = np.zeros(graph.order(), dtype='u4')

    # Store predecessors
    preds = np.empty(graph.order(), dtype='O')

    # Number of shortest paths
    sigma = np.zeros(graph.order(), dtype='u4')
    sigma[source] = 1

    # Enqueue source and mark it as visited
    Q.enqueue(source)
    visits[source] = 1

    while not Q.isempty():
        current = Q.dequeue()

        if preds[current] is not None:
            for pred in preds[current]:
                sigma[current] += sigma[pred]

        if current == target:
            break

        neighbours = graph.neighbours(current)[0]

        for neighbour in neighbours:
            if visits[neighbour] == 0:
                visits[neighbour] = visits[current] + 1
                Q.enqueue(neighbour)
                preds[neighbour] = [current]
            # Check if level of the current node is equal to the level of 
            # neighbour's parents, to find multiple shortest paths
            # Shortcut of 'and' matters here
            elif neighbour != source and visits[current] == \
                visits[preds[neighbour][0]]:
                preds[neighbour].append(current)
            
    return (visits, preds, sigma)
