# Task 20 - Python
# Factorial Digit Sum

import time
from functools import reduce

# Cheeky
# import math
# print(math.factorial(100))

def factorial_finder(number):
    return reduce(lambda a, b: a * b, range(1, number + 1))

def main():
    time_start = time.time()
    factorial_hundred = factorial_finder(100)

    print("Answer: {0} => Calculated in: {1}".format(factorial_hundred, (time.time() - time_start)))

if __name__ == '__main__':
    main()