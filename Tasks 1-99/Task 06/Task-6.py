# Task 6 - Python
# Sum Square Difference

import math
import time

def square_values():
    # Sqaure Individually
    total_i = 0
    for i in range(0, 101, 1):
        product = math.pow(i, 2)
        total_i += product

    # Sqaure as a sum
    total_s = 0
    for j in range(0, 101, 1):
        total_s += j
    product = math.pow(total_s, 2)

    return product, "-", total_i, "= ", product - total_i


def main():
    time_start = time.time()
    sqaure_products = square_values()

    print("Answer: {0} => Calculated in: {1}".format(sqaure_products, (time.time() - time_start)))

if __name__ == '__main__':
    main()
