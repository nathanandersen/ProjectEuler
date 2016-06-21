# Problem 357
from utils import sieve
from utils import is_prime
from utils import factors
# Note that for this to be the case,
# n cannot be divisible by any square number

# 100 million cannot be brute-forced.
# so these numbers must have some special property.

#if gcd(k/f,f) is not 1, then false

#Therefore the only numbers to consider are ones that are made up
#of combinations of primes

#The prime factorization of n must equal n in order for us
#to even consider it
#Must be divisible by 2 but not 4.
#Cannot be divisible by 7
#Cannot be divisible by 13
#Cannot be divisible by 23

def isPrimeGenerating(n):
    fs = factors(n)
    for f in fs:
        if not is_prime(f + int(n/f)):
            return False
    return True


total = 0
for n in range(2,100000000,4):
    if n % 7 != 0 and n % 13 != 0 and n % 23 != 0:
        # I'm not sure if this test is fair...
        # perform our test
        if isPrimeGenerating(n):
            print(n)
            total += n

print(total)

#30 = 2 * 3 * 5
#not 60
#42 = 2 * 3 * 7
