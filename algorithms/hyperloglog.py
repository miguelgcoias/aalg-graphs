import numpy as np

"""
bits are indexed from 1 to nbits as follows
x_31 x_30 ... x_1 x_0
"""

def leftmost_one(x, l, r):
    for i in range(l, r-1, -1):
        if x & 2 ** i != 0:
            return i
    return r-1

def hyperloglog(b, h):
    m = 2 ** b
    r = np.zeros(m, dtype=np.uint32)

    nbits = 32
    for x in stream:
        k = h(x)
        j = leftmost_one(k, nbits-1, )
        w = x & (2**(32-b) - 1)
        r[j] = max(r[j], leftmost_one(w)-b)

    E = 0
    for j in range(m):
        E += 2 ** (-r[j])

    E = alpha(m) * m**2 / E

    # Error Corrections
    if 2*E <= 5*m:
        V = 0
        for i in range(m):
            if r[i] == 0:
                V + 1
        if V != 0:
            E = m*log(m / V)

    if 30*E > 2**32:
        E = -2**32 * log(1 - E/2**32)

    return E
