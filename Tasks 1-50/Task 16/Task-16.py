# Task 16 - Python
# Power Digit Sum

import math
import time

def pds():
    return sum([int(num) for num in str(int(math.pow(2, 1000)))])

def main():
    time_start = time.time()
    pds_value = pds()

    print("Answer: {0} => Calculated in: {1}".format(pds_value, (time.time() - time_start)))

if __name__ == '__main__':
    main()