# Task 7 - Python
# 10001st Prime

import math
import time

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

def main():
    time_start = time.time()
    nth_prime = prime(10001)

    print("Answer: {0} => Calculated in: {1}".format(nth_prime, (time.time() - time_start)))

if __name__ == '__main__':
    main()
