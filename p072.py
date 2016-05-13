# Problem 72
from utils import gcd
from utils import factor_count

# notes:
# primes introduce p-1 new fractions

# composites introduce phi more, where phi = the number
# of relatively prime #s less than n



def find_counting_fractions(n):
    count = 0
    for a in range(1,n+1):
        for b in range(1,a):
            if 1 == gcd(a,b):
                count += 1
    return count

def find_counting_frac(n):
    if n == 1: return 0
    else: return n - factor_count(n) + find_counting_frac(n-1)

for n in range(1,20):
    print(find_counting_fractions(n))
    print(factor_count(n))
#    print(find_counting_frac(n))

# a(n) = a(n-1) + n - factors(n)
