# Task 15 - Python
# Lattice Paths

import time
from functools import reduce

binomial = lambda grid_size: reduce(lambda hoz, vert: hoz * vert, range(1, grid_size + 1), 1)

def path_route_finder(grid_size_to_check):
    # As size is perfect cube - I have limited calculations instead of n & m
    size = grid_size_to_check
    if grid_size_to_check == 0: return 1

    return binomial(2*size) // binomial(size) // binomial(size)

def main():
    time_start = time.time()
    route_num = path_route_finder(20)

    print("Answer: {0} => Calculated in: {1}".format(route_num, (time.time() - time_start)))

if __name__ == '__main__':
    main()