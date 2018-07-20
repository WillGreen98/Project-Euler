# Task 22 - Python
# Name Scores

import time
import string

names_list = sorted(open("pe22_data_set.txt").read().replace("", '').split(','))

def letter_value(name):
    return sum(string.ascii_uppercase.index(i) + 1 for i in name.strip('"'))

def name_score():
    return sum(key * letter_value(value) for key, value in enumerate(names_list, 1))

def main():
    time_start = time.time()
    name_score_value = name_score()

    print("Answer: {0} => Calculated in: {1}".format(name_score_value, (time.time() - time_start)))

if __name__ == '__main__':
    main()