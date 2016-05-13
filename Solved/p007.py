# Problem 7

# real 0m0.230s
# user 0m0.209s
# sys  0m0.012s

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
