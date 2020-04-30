import numpy as np

def tail_length(x):
    n = np.int64(0)
    while x % 2 ** (n+1) == 0:
        n += 1
    return n

def flajolet_martin(stream, hash_functions, group_size=1):
    k = len(hash_functions)
    r = np.zeros(k, dtype=np.int64)

    for x in stream:
        for i in range(k):
            h = hash_functions[i]
            r[k] = max(r[k], tail_length(h(x)))

    assert k % group_size == 0
    n_groups = k // group_size
    group_average = np.empty(n_groups, dtype=np.double)
    
    for idx in range(k):
        group_average[idx // group_size] += r[idx]

    for idx in range(n_groups):
        groups_average[idx] /= group_size

    np.sort(groups_average)

    if n_groups % 2 == 0:
        ret = groups_average[n_groups // 2 + 1]
        ret += groups_average[n_groups // 2]
        ret /= 2
    else:
        ret = groups_average[n_groups // 2 + 1]

    ret = 2**ret

    return ret
