# Task 14 - Python
# Longest Collatz sequence

import time

n_even = lambda n: n/2
n_odd = lambda n: (3 * n) + 1

def collatz_seq():

    return 0

def main():
    time_start = time.time()
    collatz_sequence = collatz_seq()

    print("Answer: {0} => Calculated in: {1}".format(collatz_sequence, (time.time() - time_start)))

if __name__ == '__main__':
    main()