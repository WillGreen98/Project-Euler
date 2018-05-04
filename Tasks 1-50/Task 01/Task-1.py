# Task 1 - Python
# Multiples of 3 and 5

import math

count_T = 0

for i in range(math.pow(10,3)):
    if i % 3 == 0 or i % 5 == 0:
        count_T += i
    print(i)
print(count_T)
    