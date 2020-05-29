import os
from time import time
from functools import partial

from structs.graph import Graph
from hash.functions import jenkins32
from algorithms.hyperball import hyperball, m_hyperball

if __name__ == '__main__':
    for graph_path in os.listdir('examples/random_worst_case'):
        if graph_path.endswith('.json'):
            name = graph_path[:-5].split('_') # get (vertices, edges, diameter)
            graph = Graph('examples/random_worst_case/' + graph_path)

            start = time()
            l = hyperball((graph, jenkins32))

            print('{} {} {}'.format(graph.order(),int(name[2]), time()-start))
