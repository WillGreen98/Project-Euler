# Task 3 - Python
# Largest Prime Factor

import math
import time

modulo = lambda x, y: x % y == 0

def lpf():
    fp_c = 2
    num_to_check = 600851475143

    while math.pow(fp_c, 2) < num_to_check:
        if modulo(num_to_check, fp_c):
            num_to_check //= fp_c
        fp_c += 1
    return num_to_check

def main():
    time_start = time.time()
    lowest_prime = lpf()

    print("Answer: {0} => Calculated in: {1}".format(lowest_prime, (time.time() - time_start)))


if __name__ == '__main__':
    main()