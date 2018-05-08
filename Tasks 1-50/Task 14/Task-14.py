# Task 14 - Python
# Longest Collatz sequence

import time

collatz_rule = lambda n: n / 2 if n % 2 == 0 else ((3 * n) + 1)

def collatz_seq():
    cache = [0, 0]

    for i in range(1000000):
        num = collatz_rule(i)

        if num > cache[0]:
            cache[0] = num
            cache[1] = i

    return cache[0], "contains Collatz terms: ", cache[1]

def main():
    time_start = time.time()
    collatz_sequence = collatz_seq()

    print("Answer: {0} => Calculated in: {1}".format(collatz_sequence, (time.time() - time_start)))

if __name__ == '__main__':
    main()