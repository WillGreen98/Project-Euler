# Task 9 - Python
# Special Pythagorean Triplet

import math
import time

num_to_check = 1000

def pythagorean_triple():
    for a in range(1, num_to_check):
        for b in range(1, num_to_check):
            for c in range(1, num_to_check):
                if((a + b + c) == num_to_check) and ((math.pow(a, 2)) + math.pow(b, 2) == math.pow(c, 2)):
                    print("A: {0} B: {1} C :{2}".format(a, b, c))
                    return a * b * c

def main():
    time_start = time.time()
    triple = pythagorean_triple()

    print("Answer: {0} => Calculated in: {1}".format(triple, (time.time() - time_start)))

if __name__ == '__main__':
    main()