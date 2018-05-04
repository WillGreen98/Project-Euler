# Task 7 - Python
# 10001st Prime

import math

primes = []

def is_prime(n):
    if n % 2 == 0 and n > 2: return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def prime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n -= 1
            if n == 0: return i
        i += 1
    return -1

print(prime(10001))