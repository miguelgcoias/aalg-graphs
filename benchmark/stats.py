import sys
path = sys.argv[1]

obj = []
with open(path) as data:
    for line in data:
        if line[0] == '#':
            continue
        obj += [float(line)]

import statistics
print(statistics.mean(obj))
print(statistics.pstdev(obj))

