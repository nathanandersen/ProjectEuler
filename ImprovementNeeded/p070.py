# Problem 70

from utils import is_prime,__primes
import sys

_phi = {1:1}

def phi_one_factor(p,n):
    if p**n in _phi:
        return _phi[p**n]
    result = p**(n-1) * (p-1)
    _phi[p**n] = result
    return p**(n-1) * (p-1)

def phi(n):
    """ The Eulerian totient."""
    if n in _phi:
        return _phi[n]
    if n == 1:
        return 1
    if is_prime(n):
        _phi[n] = n-1
        return n-1
    result = 1
    for p in __primes:
        if not(n % p):
            break
    # If p does not divide, then ignore p
    factor_count = 1
    while (n % (p ** factor_count) == 0):
        factor_count += 1
    factor_count -= 1 # 1 too-many

    result = phi_one_factor(p,factor_count) * phi(n // (p**factor_count))
    _phi[n] = result
    return result

# Hideously, way too slow.
# We need to find a more effective way of doing this.
def phi_ratio_if_is_perm(n):
    val = phi(n)
    l = list(str(val))
    _l = list(str(n))
    if sum([int(d) for d in l]) != sum([int(d) for d in _l]):
        return 2
    if set(l) == set(_l):
        if sorted(l) == sorted(_l):
            return n/val
    return 2 # if no good

min_index = 0
min_val = sys.maxsize
for n in range(3,10**7,2):
#for n in reversed(range(3,10**7,2)):
    v = phi_ratio_if_is_perm(n)
    if v < min_val:
        print(n,v)
        (min_index,min_val) = (n,v)

print(min_index,min_val)
# Hits the min value, but keeps going
#8319823
