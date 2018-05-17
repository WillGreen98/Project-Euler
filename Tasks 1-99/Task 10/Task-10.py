# Task 10 - Python
# Summations Of Primes

import math
import time

is_prime = lambda num_to_check: all(num_to_check % i for i in range(3, int(math.sqrt(num_to_check)) + 1, 2))

def sum_of_primes(upper_bound):
    fp_c = 2
    summation = 0
    eratosthenes_sieve = ((upper_bound + 1) * [True])

    while math.pow(fp_c, 2) < upper_bound:
        if is_prime(eratosthenes_sieve[fp_c]):
            multiple = fp_c * 2
            while multiple < upper_bound:
                eratosthenes_sieve[multiple] = False
                multiple += fp_c
        fp_c += 1

    for i in range(fp_c, upper_bound + 1):
        if eratosthenes_sieve[i]:
            summation += 1
    return summation

def main():
    time_start = time.time()
    prime_sum = sum_of_primes(11)

    print("Answer: {0} => Calculated in: {1}".format(prime_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()