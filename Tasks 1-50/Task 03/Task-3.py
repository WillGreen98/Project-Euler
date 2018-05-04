# Task 3 - Python
# Largest Prime Factor

num_to_check = 600851475143
is_prime = lambda is_prime: return all(nc % i for i in xrange(2, nc))

def lpf():
    for i in range(1, 1000000000, 1):
        cnum = num_to_check / i
        if isinstance(cnum, int):
            primeNum_c = is_prime(cnum)
            if primeNum_c == True: print("{0} is prime".format(primeNum_c))
            primeNum_i = is_prime(i)
            if primeNum_i == True: print("{0} is prime".format(primeNum_i))