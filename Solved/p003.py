# Problem 3

# real 0m0.192s
# user 0m0.153s
# sys  0m0.029s

from utils import sieve
import math

target = 600851475143
primes = sieve(int(math.sqrt(target)))
print(max(p for p in primes if not target%p))
