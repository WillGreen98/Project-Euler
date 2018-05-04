# Task 5 - Python
# Smallest Multiple

import math
from functools import reduce

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, math.fmod(a, b))

def lcm(a, b):
    return (a * b) / gcd(a, b)

print(int(reduce(lcm, range(1, 20, 1))))