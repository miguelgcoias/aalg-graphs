import warnings

# Assumes 32 bit keys
mask = 2**32-1

def linear(x, a, b):
    warnings.filterwarnings('ignore')
    return (a*x + b) & mask

def magic(x):
    warnings.filterwarnings('ignore')
    x = x & mask
    x = (((x >> 16) ^ x) * 0x45d9f3b) & mask
    x = (((x >> 16) ^ x) * 0x45d9f3b) & mask
    x =  (x >> 16) ^ x
    return x

def jenkins32(a):
    a = ((a+0x7ed55d16) + (a<<12)) & mask
    a = (a^0xc761c23c) ^ (a>>19)
    a = ((a+0x165667b1) + (a<<5)) & mask
    a = ((a+0xd3a2646c) ^ (a<<9)) & mask
    a = ((a+0xfd7046c5) + (a<<3)) & mask
    a = (a^0xb55a4f09) ^ (a>>16)
    return a;

def hash32shift(x):
    x = (x << 15) & mask - x - 1
    x = (x + (x << 2)) & mask
    x = x ^ (x >> 4)
    x = (x * 2057) & mask

def mix(a, b, c):
  a = a-b
  a = a-c
  a = a ^ (c >> 13)
  b = b-c
  b = b-a
  b = (b ^ (a << 8)) & mask
  c = c-a
  c = c-b
  c = c ^ (b >> 13)
  a = a-b
  a = a-c
  a = a ^ (c >> 12)
  b = b-c
  b = b-a
  b = (b ^ (a << 16)) & mask
  c = c-a
  c = c-b
  c = c ^ (b >> 5)
  a = a-b
  a = a-c
  a = a^(c >> 3)
  b = b-c
  b = b-a
  b = (b ^ (a << 10)) & mask
  c = c-a
  c = c-b
  c = c ^ (b >> 15)
  return c
