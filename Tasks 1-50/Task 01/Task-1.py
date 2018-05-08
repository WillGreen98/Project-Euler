# Task 1 - Python
# Multiples of 3 and 5

import math
import time

def mul_three_five():
    count_T = 0

    for i in range(int(math.pow(10, 3))):
        if i % 3 == 0 or i % 5 == 0:
            count_T += i
    return count_T

def main():
    time_start = time.time()
    count_T = mul_three_five()

    print("Answer: {0} => Calculated in: {1}".format(count_T, (time.time() - time_start)))

if __name__ == '__main__':
    main()