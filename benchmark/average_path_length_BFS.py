import os
import sys
import numpy as np

from structs.graph import Graph
from benchmark.utils import plot, measure
from algorithms.average_path_length import average_path_length

# Set arguments
args = {'ylabel': 'Runtime (s)',
        'xlabel': 'V(V+E)'}

# Find graphs to test
graph_paths = []
for g in os.listdir('./examples/undirected'):
    if g.endswith('.json'):
        graph_paths.append(g)

num_graphs = len(graph_paths)
sizes = np.empty(num_graphs, dtype=np.int64)
times = np.empty(num_graphs, dtype=np.double)
apl = lambda g: average_path_length(g, algorithm="BFS")
n_runs, n_repeats = int(sys.argv[1]), int(sys.argv[2])

# Run the algorithm
for idx, g in enumerate(graph_paths):
    print(g.upper())
    graph = Graph('examples/undirected/' + g)
    sizes[idx] = graph.order() * (graph.order() + graph.size())
    times[idx] = measure(apl, graph, n_runs=n_runs, n_repeats=n_repeats)

plot(sizes, times, args)
print("OK")
