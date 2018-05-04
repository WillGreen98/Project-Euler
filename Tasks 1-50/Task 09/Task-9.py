# Task 9 - Python
# Special Pythagorean Triplet

import math

for a in range(0, 333):
    for b in range(0, 333):
        for c in range(0, 333):
            if((a + b + c) == 1000) and ((math.pow(a, 2)) + math.pow(b, 2) == math.pow(c, 2)):
                print(a* b * c)