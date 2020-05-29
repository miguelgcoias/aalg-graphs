import os
import sys
import math
import statistics
from time import time
from random import randint
from functools import partial

from structs.graph import Graph
from hash.functions import linear, mix
from algorithms.hyperball import hyperball, m_hyperball


################################################################################

def rand(x):
    return randint(0, 2**32)

def urand(x):
    return sum([a << (24 - 8*i) for i,a in enumerate(os.urandom(4))])

def random():
    return rand

def urandom():
    return urand

def get_linear():
    return partial(linear, a=randint(0, 2**32), b=randint(0,2**32))

def get_mix():
    return partial(mix, a=randint(0, 2**32), b=randint(0,2**32))

def get_colinear():
    a1 = randint(0, 2**32)
    b1 = randint(0, 2**32)
    while math.gcd(a1,b1) != 1:
        a1 = randint(0, 2**32)
        b1 = randint(0, 2**32)
    return partial(linear, a=a1, b=b1)

################################################################################


graph_names = ['US Power Grid', 'PGP', 'random1', 'random2', 'random3']
paths = ['examples/uspowergrid.json', 'examples/pgp.json',
        'examples/26988_314915_5.json', 'examples/37129_301192_6.json', 'examples/49056_416086_6.json']

hash_names = ['RANDOM', 'URANDOM', 'LINEAR', 'MIX', 'COLINEAR']
hash_family = [random, urandom, get_linear, get_mix, get_colinear]

idx1 = int(input("GRAPH: "))
idx2 = int(input("HASH FAMILY: "))

graph_name = graph_names[idx1]
graph = Graph(paths[idx1])

h_name = hash_names[idx2]
h = hash_family[idx2]()

f = open(sys.argv[1], 'a')

for i in range(700):
    print(i)
    h = hash_family[idx2]()
    f.write(str(hyperball((graph,h))))
    f.write('\n')
