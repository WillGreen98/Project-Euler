# Task 4 - Python
# Largest Palindrome Product

palindromes = []

def palindrome_check(number):
    return bool(str(number) == str("{0}".format(number)[::-1]))

def largestPalindrome():
    for i in range(100, 999, 1):
        for j in range(100, 999, 1):
            product = i * j
            if palindrome_check(product):
                palindromes.append(product)
    return max(palindromes)

print(largestPalindrome())

