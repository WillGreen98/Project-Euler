# Task 8 - Python
# Largest Product In A Series

import time
from functools import reduce

number = [[int, line.split()] for line in open('pe08_data_set.txt').readlines()]

def lps():
    return (max([reduce(lambda sum, x:
                        sum * x, [int(x)
                                  for x in number[i:i + 5]])
                 for i in range(len(number) - 5)]))

def main():
    time_start = time.time()
    largest_product = lps()

    print("Answer: {0} => Calculated in: {1}".format(largest_product, (time.time() - time_start)))


if __name__ == '__main__':
    main()
