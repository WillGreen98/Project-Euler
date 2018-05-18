# Task 17 - Python
# Number letter counts

import math
import time

num_ln = {1: "One",
          2: "Two",
          3: "Three",
          4: "Four",
          5: "Five",
          6: "Six",
          7: "Seven",
          8: "Eight",
          9: "Nine"}

def count_letters(num_to_check):
    num_list = list(map(int, str(num_to_check)))

    count = 0
    for i in range(1, 1000, 1):
        for n in num_list:
            word_length = len(num_ln[n])
            count += word_length
    return count

def main():
    time_start = time.time()
    letters_count = count_letters()

    print("Answer: {0} => Calculated in: {1}".format(letters_count, (time.time() - time_start)))

if __name__ == '__main__':
    main()