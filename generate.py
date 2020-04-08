from json import dump
from random import randint, sample


def generate(n, path, density):
    '''Generates JSON files representing random directed graphs.

    Keyword arguments:
    n: number of vertices.
    path: path to JSON file.
    density: maximum number of edges of any vertex.'''
    adj = dict.fromkeys(range(n))
    
    for v in range(n):
        adj[v] = sample(range(n), randint(1, density))

    with open(path, 'w') as graph:
        dump(adj, graph, indent=4)

generate(10**7, 'examples/fix.json', 5)
