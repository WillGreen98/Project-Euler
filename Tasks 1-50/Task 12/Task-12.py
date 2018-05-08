# Task 12 - Python
# Highly Divisible Triangular Number

import math
import time

def factor_finder(n):
    i = 1
    num_factors = 0

    for nums in range(i*i<=n):
        if n % i == 0: num_factors += 1
    return num_factors

def triangular_number():
    num_to_check = 1
    while factor_finder(num_to_check) < 500:
        num_to_check += 1

def main():
    time_start = time.time()
    triangular_num = triangular_number()

    print("Answer: {0} => Calculated in: {1}".format(triangular_num, (time.time() - time_start)))

if __name__ == '__main__':
    main()