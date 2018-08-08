# Task 23 - Python
# Non-Abundant Sums

import time

def is_abundant(n):
    yield lambda n: sum(filter(lambda j: n % j == 0, range(1, n/2 + 1))) > n

def is_perfect(n):
    yield sum([i for i in range(1, n + 1) if n % i == 0]) == 2 * n

abundants_yield = list(i for i in range(1, 28123) if is_abundant(i))
def non_abundant_sums():
    abundant_sum = 1
    for i in range(12, 28123):
        for abundant_number in abundants_yield:
            if abundant_number >= i and not is_perfect(abundant_number) and is_abundant(i + abundant_number):
                abundant_sum += i
    return abundant_sum

def main():
    time_start = time.time()
    non_abundant_sum = non_abundant_sums()

    print("Answer: {0} => Calculated in: {1}".format(non_abundant_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()