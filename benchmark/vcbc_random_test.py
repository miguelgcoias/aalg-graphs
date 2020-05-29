import timeit
import os

from structs.graph import Graph
from algorithms.vcbc import vcbc


random_path = os.path.join('examples', 'random')
graphs = os.listdir(random_path)
print(graphs)

for graph in graphs:
    name = graph.rstrip('\n')
    # Test only graphs with diameter 6
    if name[-7:] == '_6.json':
        print(f'{name.rstrip(".json")}: ' + str(timeit.timeit('vcbc(g, 0.05, 0.1)',
        setup=f'import gc; gc.enable(); g = Graph(\'{os.path.join(random_path, name)}\')',
        globals=globals(), number=3) / 3))