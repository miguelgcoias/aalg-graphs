import timeit

from algorithms.vcbc import vcbc
from structs.graph import Graph

if __name__ == '__main__':
    # Run with varying epsilon
    eps_values = [0.1, 0.08, 0.06, 0.04, 0.02]
    paths = ['examples/uspowergrid.json', 'examples/amazon.json',
    'examples/hyves.json']

    # US power grid
    for eps in eps_values:
        print(f'uspowergrid, {eps}: ' + str(timeit.timeit(f'vcbc(uspg, {eps}, \
        0.1)', setup=f'import gc; gc.enable(); \
        uspg = Graph(\'{paths[0]}\')', globals=globals(), number=3)/3))

    # Amazon
    for eps in eps_values:
        print(f'amazon, {eps}: ' + str(timeit.timeit(f'vcbc(amazon, {eps}, \
        0.1)', setup=f'import gc; gc.enable(); \
        amazon = Graph(\'{paths[1]}\')', globals=globals(), number=3)/3))
    
    # Hyves
    for eps in eps_values:
        print(f'hyves, {eps}: ' + str(timeit.timeit(f'vcbc(hyves, {eps}, \
        0.1)', setup=f'import gc; gc.enable(); \
        hyves = Graph(\'{paths[2]}\')', globals=globals(), number=3)/3))