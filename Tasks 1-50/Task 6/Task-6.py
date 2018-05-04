# Task 6 - Python
# Sum Square Difference

import math

# Sqaure Individually
total_i = 0
for i in range(0, 101, 1):
    product = math.pow(i, 2)
    total_i += product

# Sqaure as a sum
total_s = 0
for j in range(0, 101, 1):
    total_s += j
product = math.pow(total_s, 2)

print(product, " - ", total_i, " = ", product - total_i)