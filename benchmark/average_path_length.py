import os
from structs.graph import Graph
from benchmark.utils import plot, measure
from algorithms.average_path_length import average_path_length

sizes = []
times = []

for g in os.listdir('./examples'):
    if g.endswith('.json'):
        print('examples/' + g)
        G = Graph('examples/' + g)
        sizes.append(G.order() * (G.order() + G.size()))
        times.append(measure(average_path_length, G, n_repeats=10))

plot(sizes, times)
print("OK")
