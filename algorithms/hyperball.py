def hyper_ball(graph):
    n = graph.order()

    distance_sum = 0
    counters = [HyperLogLogCounter(5) for j in range(n)]

    for r in range(n):
        for v in range(n):
            delta = -counters[v].size()
            for u in v.neighbours():
                counters[v].union(counters[u])
            delta += counters[v].size()

            distance_sum += r * delta

    apl = distance_sum / (n * (n-1))
    return apl
