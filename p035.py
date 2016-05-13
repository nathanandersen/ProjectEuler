# Problem 35
from utils import is_prime

global primes
primes = [x for x in range(1000000) if is_prime(x)]
def is_rotatable(p):
    for a in range(1,len(p)):
        if (int(p[a:]+p[:a]) not in primes):
            return False
    return True

rotatable_primes = [p for p in primes if is_rotatable(str(p))]

print(len(rotatable_primes))
