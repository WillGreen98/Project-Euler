# Task 10 - Python
# Summations Of Primes

# Task 3 is_prime Code Copy
is_prime = lambda is_prime: return all(nc % i for i in xrange(2, nc))

summation = 0
number_to_check = 0

for i in range(0, 2000000):
    if is_prime(number_to_check):
        summation += number_to_check
    print(summation)
