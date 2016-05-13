# Problem 47
from utils import prime_factors

def solve():
    n = 647
    while(n):
        if(len(prime_factors(n)) == 4 and
           len(prime_factors(n+1)) == 4 and
           len(prime_factors(n+2)) == 4 and
           len(prime_factors(n+3)) == 4):
            return n
        n += 4

print(solve())
