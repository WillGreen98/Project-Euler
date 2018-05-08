# Task 3 - Python
# Largest Prime Factor

import time

num_to_check = 600851475143
is_prime = lambda is_prime: all(num_to_check % i for i in range(2, num_to_check))

def lpf():
    for i in range(1, 1000000000, 1):
        cnum = num_to_check / i
        if isinstance(cnum, int):
            primeNum_c = is_prime(cnum)
            if primeNum_c == True: print("{0} is prime".format(primeNum_c))
            primeNum_i = is_prime(i)
            if primeNum_i == True: print("{0} is prime".format(primeNum_i))

def main():
    time_start = time.time()
    lowest_prime = lpf()

    print("Answer: {0} => Calculated in: {1}".format(lowest_prime, (time.time() - time_start)))

if __name__ == '__main__':
    main()