import numpy as np

b = 5
p = 2 ** b
mask = 2 ** b - 1
alpha = 0.697

def hyperball(graph, hash_functions, eps=10**-9):
    n = graph.order()

    distance_sum = 0
    counters = [np.zeros(p, dtype=np.uint32) for j in range(n)]

    #TODO
    h = hash_functions[0]

    for v in range(n):
        add(counters[v], h(v))
        print("LOL")
        print(counters[v][0])

    for r in range(n):
        print(r)
        for v in range(n):
            delta = -size(counters[v])
            for u in graph.neighbours(v):
                union(counters[v], counters[u])
            delta += size(counters[v])
            distance_sum += r * delta

        if delta < eps:
            break

    apl = distance_sum / (n * (n-1))
    return apl

def union(counter1, counter2):
    for i in range(p):
        counter1[i] = max(counter1[i], counter2[i])

def size(counter):
    ret = 0
    for j in range(p):
        ret += 2 ** -counter[j]

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
