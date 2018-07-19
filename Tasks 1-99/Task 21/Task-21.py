# Task 21 - Python
# Amicable Numbers

import time
from functools import reduce

def d(n):
        return sorted(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))[:-1]

def amicable_numbers_check(m, n):
    return "{0} & {1} => {2}".format(m, n, sum(d(m)) == n and n != m)

def d_calculate():
    total = 0


def main():
    time_start = time.time()

    print(d(220))
    print(d(284))
    print(amicable_numbers_check(220, 284))

    amicable_numbers = d_calculate()
    print("Answer: {0} => Calculated in: {1}".format(amicable_numbers, (time.time() - time_start)))

if __name__ == '__main__':
    main()