# Task 10 - Python
# Summations Of Primes

import time

num_to_check = 0
is_prime = lambda is_prime: all(num_to_check % i for i in range(2, num_to_check)) # Task 3 is_prime Code Copy

def sum_of_primes():
    summation = 0

    for i in range(0, 2000000):
        if is_prime(num_to_check):
            summation += num_to_check
        return summation

def main():
    time_start = time.time()
    prime_sum = sum_of_primes()

    print("Answer: {0} => Calculated in: {1}".format(prime_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()