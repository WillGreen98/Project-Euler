# Task 4 - Python
# Largest Palindrome Product

import time

palindromes = []

def palindrome_check(number):
    return bool(str(number) == str("{0}".format(number)[::-1]))

def largestPalindrome():
    for i in range(100, 999, 1):
        for j in range(100, 999, 1):
            product = i * j # Mathematically = xyz * abc
            if palindrome_check(product):
                palindromes.append(product)
    return max(palindromes)

def main():
    time_start = time.time()
    largest_palindrome = largestPalindrome()

    print("Answer: {0} => Calculated in: {1}".format(largest_palindrome, (time.time() - time_start)))

if __name__ == '__main__':
    main()