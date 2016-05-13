#Problem 50

# real 0m1.834s
# user 0m1.765s
# sys  0m0.042s

from utils import sieve
from utils import is_prime

primes = sieve(1000000)

max_primes = 1
for x in range(78498-50):
    for y in range(499,600):
        total = sum(primes[x+z] for z in range(y))
        if total in primes and y > max_primes:
            print(y,total)
            max_primes = y
print(max_primes)
