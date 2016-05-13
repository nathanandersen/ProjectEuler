# Problem 7
# Find the 10,001st prime number
import math
from utils import is_prime

#linear search
def find_primes():
    count = 0
    i = 1
    while (count < 10001):
        i += 1
        if is_prime(i):
            count += 1
    return i

print (find_primes())
