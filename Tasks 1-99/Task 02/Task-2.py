# Task 2 - Python
# Sum of even fib nums

import time

nums = {}

def fibonacci(n):
    fn_1, fn_2 = 1, 1
    for i in range(n - 1):
        fn_1, fn_2 = fn_2, fn_1 + fn_2
    return fn_1

def fib(fib_n, fib_c):
    if fib_c not in nums:
        nums[fib_c] = fib_n(fib_c)
        return nums[fib_c]

def sum_even_fib():
    fib_total = 0
    fib_even = lambda fn: (fn % 2 == 0)

    for i in range(0, 4000000, 1):
        fibn = fib(fibonacci, i)

        if fib_even(fibn):
            fib_total += fibn
    return fib_total

def main():
    time_start = time.time()
    fib_sum = sum_even_fib()

    print("Answer: {0} => Calculated in: {1}".format(fib_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()




