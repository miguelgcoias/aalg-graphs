import warnings

def linear(x, a, b, m):
    warnings.filterwarnings('ignore')
    return (a*x + b) % m

# Assumes 32 bit keys
def magic(x, m):
    warnings.filterwarnings('ignore')
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x =  (x >> 16) ^ x
    return x % m
