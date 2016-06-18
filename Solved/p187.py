# Problem 187

#real	0m9.912s
#user	0m8.388s
#sys	0m1.383s

# The slowest part of this is the sieve.

from utils import sieve

def semiprimeCount(n):
    _primes = sieve(n//2)
    total = 0
    for p in _primes:
        if p**2 >= n:
            return total
        for index in reversed(range(len(_primes))):
            if p* _primes[index] < n:
                # Once we are within the range, preserve all the primes
                # but remove the first (to prevent overcounting)
                _primes = _primes[1:index+1:] # Keep that last one inclusive
                total += index+1
                break
    return total

target = 100000000
total = semiprimeCount(target)
print(total)
