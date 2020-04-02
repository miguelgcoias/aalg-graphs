import numpy as np
from structs.graph import Graph
from structs.disjointset import DisjointSet

def boruvka(G):
    n, m = G.order(), G.size()
    edges = G.edges()
    ds = DisjointSet(n)

    ret = np.empty(n, dtype='O')
    min_edge = np.empty(m, dtype=int)
    min_weight = np.empty(m, dtype=np.int32)

    components = n
    while components > 1:
        min_edge.fill(-1)
        min_weight.fill(np.iinfo(np.int32).max)

        for idx in range(m):
            v, u, w = edges[idx]
            v, u = ds.find(v), ds.find(u)

            if u == v:
                continue
            
            if min_weight[u] > w:
                min_weight[u] = w
                min_edge[u] = idx

            if min_weight[v] > w:
                min_weight[v] = w
                min_edge[v] = idx

            for idx in range(n):
                v, u, w = edges[idx]
                if ds.find(u) != ds.find(v):
                    ds.union(u, v)
                    components -= 1
                    ret[components] = edges[idx]
        return ret


    


















    num_runs = np.ceil(2 + (G.order() * (G.order() - 1) * 
    np.log2(G.order())) / 2).astype(np.int64)

    min_cut = G.size() + 1
    for i in range(num_runs):
        min_cut = min(min_cut, contract(G))

    return min_cut

def contract(G):
    edges = G.edges()
    ds = DisjointSet(G.order())
    order = np.random.permutation(G.size())

    edge_idx = 0

    for n in range(G.order() - 2):
        # Contract graph
        while edge_idx < G.size():
            u, v = edges[order[edge_idx]]
            edge_idx += 1

            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                break

    cut = 0
    for e in edges:
        if ds.find(e[0]) != ds.find(e[1]):
            cut += 1

    return cut

G = Graph('examples/example2.json')
print(karger(G))
