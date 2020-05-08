import numpy as np

b = 5
p = 2 ** b
alpha = 0.697

def hyper_ball(graph, hash_functions):
    n = graph.order()

    distance_sum = 0
    counters = [np.zeros(p, dtype=np.uint8) for j in range(n)]

    #TODO
    h = hash_functions[0]

    for v in range(n):
        add(counters[v], h(v))

    for r in range(n):
        for v in range(n):
            delta = -size(counters[v])
            for u in graph.neighbours(v):
                union(counters[v], counters[u])
            delta += size(counters[v])
            distance_sum += r * delta

    apl = distance_sum / (n * (n-1))
    return apl

def size(counter):
    ret = 0
    for j in range(p):
        ret += 2 ** -int(counter[j])

    ret = alpha * p**2 / ret
    return ret

def union(counter1, counter2):
    for i in range(p):
        counter1[i] = max(counter1[i], counter2[i])

def add(counter, x):
    idx = x >> (32 - b)
    counter[idx] = max(counter[idx], leading_zeros(x, left=32-b))

def leading_zeros(x, left=32, right=0):
    for i in range(left, right, -1):
        if x & 2 ** i != 0:
            return (left-i) + 1

    return (left-right) + 1
