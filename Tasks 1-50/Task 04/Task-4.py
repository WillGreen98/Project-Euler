# Task 4 - Python
# Largest Palindrome Product

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
    print(largestPalindrome())

if __name__ == '__main__':
    main()