# Problem 37
from utils import is_prime

def is_truncatable_prime(p):
    for x in range(1,len(p)):
        if not is_prime(int(p[:x])) or not is_prime(int(p[x:])):
            return False
    return True

t_primes = [p for p in range(8,1000000) if is_prime(p) and is_truncatable_prime(str(p))]

print(sum(t_primes))
