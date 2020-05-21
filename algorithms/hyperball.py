from time import time
from array import array
import multiprocessing as mp

b = 5
p = 2 ** b
mask = 2 ** b - 1
alpha = 0.697

def m_hyperball(graph, hash_functions):
    ret = 0
    pool = mp.Pool(processes=4)

    start = time()
    for x in pool.imap_unordered(hyperball, [[graph, h] for h in hash_functions]):
        ret += x
        print("{} : (Time elapsed: {}s)".format(x, int(time() - start)))

    ret /= len(hash_functions)
    return ret
    

def hyperball(data):
    graph, h = data
    n = graph.order()

    distance_sum = 0
    counters = [[array('I', [0]*p) for j in range(n)] for i in range(2)]

    for v in range(n):
        add(counters[0][v], h(v))

    for r in range(n):
        delta = 0
        for v in range(n):
            a = counters[(r+1)%2][v]
            union(a, counters[r%2][v])

            for u in graph.neighbours(v):
                union(a, counters[r%2][u])
            delta += size(a) - size(counters[r%2][v])

        distance_sum += r * delta

        if delta == 0:
            break

    apl = distance_sum / (n * (n-1))
    return apl

def union(counter1, counter2):
    for i in range(p):
        counter1[i] = max(counter1[i], counter2[i])

def size(counter):
    ret = 0
    for j in range(p):
        ret += 2 ** -float(counter[j])

    ret = alpha * p**2 / ret
    return ret

def add(counter, x):
    idx = x & mask
    counter[idx] = max(counter[idx], zeros(x >> b))

def zeros(x, max_bits=32-b):
    ret = 1
    while x & 1 == 0 and ret <= max_bits:
        ret += 1
        x >>= 1
    return ret
