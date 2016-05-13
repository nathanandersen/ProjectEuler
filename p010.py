# Problem 10
# Sum of all primes below 2 million
import math
from utils import is_prime

#c(ap)
# This is not a good implementation
def sum_primes(c):
    return 2 + sum((i if is_prime(i) else 0) for i in range(3,c,2))

print( sum_primes(2000000))
