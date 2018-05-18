# Task 12 - Python
# Highly Divisible Triangular Number

import math
import time

triangular_nth = lambda n: (n * (n + 1)) / 2

def triangular_number():
    num_to_check = 1
    while triangular_nth(num_to_check) <= 500:
        num_to_check += 1
    return num_to_check

def main():
    time_start = time.time()
    triangular_num = triangular_number()
    # triangular_num = triangular_f(7)

    print("Answer: {0} => Calculated in: {1}".format(triangular_num, (time.time() - time_start)))

if __name__ == '__main__':
    main()