# Task 24 - Python
# Lexicographic Permutations

import time
import string
from itertools import permutations

def lexicographical_permutations_cheeky():
    return ''.join(list(permutations(string.digits))[999999])


def permutation(head, tail=""):
    if len(head) == 0: print(tail)

    for i in range(len(head)):
        permutation(head[0:i] + head[i+1:], tail+head[i])

def main():
    time_start = time.time()
    #millionth_lexi_perm = permutation(string.digits)[999999]

    cheeky_spicy_lexi_perm = lexicographical_permutations_cheeky()

    print("Answer: {0} => Calculated in: {1}".format(cheeky_spicy_lexi_perm, (time.time() - time_start)))

if __name__ == '__main__':
    main()