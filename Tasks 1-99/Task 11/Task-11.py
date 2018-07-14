# Task 11 - Python
# Largest Product In Grid

import time

grid = [list(map(int, line.split())) for line in open('pe11_data_set.txt').readlines()]

def largest_four_sum():
    x = max(grid[row][col] * grid[row][col + 1] * grid[row][col + 2] * grid[row][col + 3] for row in range(20) for col in range(17))
    y = max(grid[row][col] * grid[row + 1][col] * grid[row + 2][col] * grid[row + 3][col] for row in range(17) for col in range(20))
    xy_bottom_left_up = max(grid[row][col] * grid[row + 1][col + 1] * grid[row + 2][col + 2] * grid[row + 3][col + 3] for row in range(17) for col in range(17))
    xy_top_left_down = max(grid[row][col] * grid[row - 1][col + 1] * grid[row - 2][col + 2] * grid[row - 3][col + 3] for row in range(3, 20) for col in range(17))

    return max(x, y, xy_bottom_left_up, xy_top_left_down)

def main():
    time_start = time.time()
    largest_sum = largest_four_sum()

    print("Answer: {0} => Calculated in: {1}".format(largest_sum, (time.time() - time_start)))

if __name__ == '__main__':
    main()