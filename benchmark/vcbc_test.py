import timeit

from algorithms.vcbc import vcbc
from structs.graph import Graph


if __name__ == '__main__':
    # Run with varying epsilon
    eps_values = [0.1, 0.08, 0.06, 0.04, 0.02]
    paths = ['examples/uspowergrid.json', 'examples/pgp.json',
    'examples/amazon.json', 'examples/hyves.json',
    'examples/random/49056_416086_6.json', 
    'examples/random/11120_106378_5.json']

    # # 49056_416086_6
    # for eps in eps_values:
    #     print(f'49056_416086_6, {eps}: ' + str(timeit.timeit(f'vcbc(rand, {eps}, \
    #     0.1)', setup=f'import gc; gc.enable(); \
    #     rand = Graph(\'{paths[4]}\')', globals=globals(), number=3)/3))

    # 11120_106378_5
    for eps in eps_values:
        print(f'11120_106378_5, {eps}: ' + str(timeit.timeit(f'vcbc(rand, {eps}, \
        0.1)', setup=f'import gc; gc.enable(); \
        rand = Graph(\'{paths[5]}\')', globals=globals(), number=3)/3))

    # # US power grid
    # for eps in eps_values:
    #     print(f'US power grid, {eps}: ' + str(timeit.timeit(f'vcbc(uspg, {eps}, \
    #     0.1)', setup=f'import gc; gc.enable(); \
    #     uspg = Graph(\'{paths[0]}\')', globals=globals(), number=3)/3))

    # # PGP
    # for eps in eps_values:
    #     print(f'PGP, {eps}: ' + str(timeit.timeit(f'vcbc(pgp, {eps}, \
    #     0.1)', setup=f'import gc; gc.enable(); \
    #     pgp = Graph(\'{paths[1]}\')', globals=globals(), number=3)/3))

    # # Amazon
    # for eps in eps_values:
    #     print(f'Amazon (MDS), {eps}: ' + str(timeit.timeit(f'vcbc(amazon, {eps}, \
    #     0.1)', setup=f'import gc; gc.enable(); \
    #     amazon = Graph(\'{paths[2]}\')', globals=globals(), number=3)/3))
    
    # # Hyves
    # for eps in eps_values:
    #     print(f'Hyves, {eps}: ' + str(timeit.timeit(f'vcbc(hyves, {eps}, \
    #     0.1)', setup=f'import gc; gc.enable(); \
    #     hyves = Graph(\'{paths[3]}\')', globals=globals(), number=3)/3))
