# Task 9 - Python
# Special Pythagorean Triplet

import math
import time

def pythagorean_triple():
    for a in range(0, 333):
        for b in range(0, 333):
            for c in range(0, 333):
                if((a + b + c) == 1000) and ((math.pow(a, 2)) + math.pow(b, 2) == math.pow(c, 2)):
                    return (a* b * c)

def main():
    time_start = time.time()
    triple = pythagorean_triple()

    print("Answer: {0} => Calculated in: {1}".format(triple, (time.time() - time_start)))

if __name__ == '__main__':
    main()