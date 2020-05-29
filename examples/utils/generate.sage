import os
import random
from json import dump

def generate(path):
    n = random.randint(10, 10**4)
    p = random.uniform(0.0001, 0.01)
    print(n, p)

    g = graphs.RandomGNP(n, p)

    while not g.is_connected():
        n = random.randint(10, 10**4)
        p = random.uniform(0.0001, 0.01)
        print(p)
        g = graphs.RandomGNP(n, p)

    dict = {v: [] for v in range(n)}
    for e in g.edges():
        u, v = e[:2]
        dict[int(v)].append(int(u))
        dict[int(u)].append(int(v))

    d = g.diameter()
    name = "{}_{}_{}.json".format(g.order(), g.size(), d)
    print(name)

    with open(path+'/'+name, 'w') as f:
        dump(dict, f, indent=2)

for _ in range(5 * 10**3):
    generate(sys.argv[1])
