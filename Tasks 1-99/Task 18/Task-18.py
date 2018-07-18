# Task 18 - Python
# Maximum path sum I

import math
import time

triangle = [list(map(int, line.split())) for line in open('pe18_data_set.txt').readlines()]

def path():
    # Dynamic Methods for Bottom-Up
    for row in range(len(triangle) - 1, 0, -1):
        for col in range(0, row):
            triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])
    return triangle[0][0]

def main():
    time_start = time.time()
    max_route = path()

    print("Answer: {0} => Calculated in: {1}".format(max_route, (time.time() - time_start)))

if __name__ == '__main__':
    main()