from structs.graph import Graph
from algorithms.average_path_length import average_path_length

G = Graph('examples/undirected.json')
average_path_length(G)
print("OK")
