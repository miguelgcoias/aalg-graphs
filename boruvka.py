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
