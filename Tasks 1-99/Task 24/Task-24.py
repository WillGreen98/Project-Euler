# Task 24 - Python
# Lexicographic Permutations

import time
import string
from itertools import permutations

def lexicographical_permutations_cheeky(index):
    return ''.join(list(permutations(string.digits))[index])

def permutation(data):
    lexi_temp = []

    for head in range(len(data)):
        lp = data[:head] + data[head + 1:]
        for tail in permutation(lp):
            lexi_temp.append(data[head:head + 1] + tail)
    return lexi_temp

def main():
    time_start = time.time()
    millionth_lexi_perm = permutation(string.digits)
    cheeky_lexi_perm = lexicographical_permutations_cheeky(999999)
    spicy_lexi_perm = divmod(999999, 362880)

    print("Answer: {0} => Calculated in: {1}".format(millionth_lexi_perm, (time.time() - time_start)))

if __name__ == '__main__':
    main()