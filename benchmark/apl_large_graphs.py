import os
import statistics
from time import time
from random import randint

from functools import partial
from hash.functions import mix
from structs.graph import Graph
from algorithms.hyperball import hyperball, m_hyperball

def get_mix():
    return partial(mix, a=randint(0, 2**32), b=randint(0,2**32))

paths = ['examples/uspowergrid.json', 'examples/pgp.json', 'examples/amazon.json', 'examples/hyves.json']

for path in paths:
    name = path[:-5]

    print(name)
    graph = Graph(path)

    start = time()
    m = m_hyperball(graph, [get_mix() for i in range(4)])

    print('NAME: {} | {} {} | {}'.format(name, statistics.mean(m), statistics.pstdev(m), time()-start))
