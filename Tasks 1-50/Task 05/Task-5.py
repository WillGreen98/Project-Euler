# Task 5 - Python
# Smallest Multiple

import math
import time
from functools import reduce

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, math.fmod(a, b))

def lcm(a, b):
    return (a * b) / gcd(a, b)

def main():
    time_start = time.time()
    smallest_multiple = (int(reduce(lcm, range(1, 20, 1))))

    print("Answer: {0} => Calculated in: {1}".format(smallest_multiple, (time.time() - time_start)))

if __name__ == '__main__':
    main()