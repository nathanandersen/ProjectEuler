# Problem 37

# real 0m0.482s
# user 0m0.436s
# sys  0m0.036s

from utils import is_prime
from utils import sieve

primes = [p for p in sieve(1000000)]
primes.remove(2)
primes.remove(3)
primes.remove(5)
primes.remove(7)
def is_truncatable_prime(p):
    p = str(p)
    for x in range(1,len(p)):
        if not is_prime(int(p[:x])) or not is_prime(int(p[x:])):
            return False
    return True

t_primes = [p for p in primes if is_truncatable_prime(p)]
print(sum(t_primes))
