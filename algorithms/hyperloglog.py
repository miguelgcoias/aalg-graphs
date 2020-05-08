import numpy as np


def leading_zeros(x, left=32, right=0):
    for i in range(left, right, -1):
        if x & 2 ** i != 0:
            return (left-i) + 1

    return (left-right) + 1
