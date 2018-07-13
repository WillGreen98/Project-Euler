# Task 2 - Python
# Sum of even fib nums

import time

nums = {}

def fibonacci(fib_limit):
    a, b = 1, 1
    for i in range(1, fib_limit):
        a, b = b, a + b
    return a

#  Memoize / Caching because of recursion limit being < 4000000
def fibonacci_gen(fib_limit, i):
    if i not in nums:
        nums[i] = fib_limit(i)
    return nums[i]

def sum_even_fib():
    sum = 0

    for i in range(35):
        fib_num = fibonacci_gen(fibonacci, i)
        if fib_num % 2 == 0:
            sum += fib_num
    return sum

def main():
    time_start = time.time()
    fib_sum = sum_even_fib()

    print("Answer: {0} => Calculated in: {1}".format(fib_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()