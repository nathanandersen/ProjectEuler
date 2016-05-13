# Problem 35

# real 0m0.818s
# user 0m0.769s
# sys  0m0.038s

from utils import is_prime
from utils import sieve

primes = [p for p in sieve(1000000)]
def is_rotatable(p):
    for a in range(1,len(p)):
        if not is_prime(int(p[a:]+p[:a])):
            return False
    return True

rotatable_primes = [p for p in primes if is_rotatable(str(p))]

print(len(rotatable_primes))
