# Problem 3
# What is the largest prime factor of the number
# 600851475143
from utils import sieve
import math

target = 600851475143
primes = sieve(int(math.sqrt(target)))
print(max(p for p in primes if not target%p))
