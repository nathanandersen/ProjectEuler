#Problem 51

# real 0m17.179s
# user 0m16.451s
# sys  0m0.284s

from utils import sieve
import sys
from utils import is_prime

primes = sieve(1000000)
candidates = [p for p in primes if p > 1000]
digits = [0,1,2,3,4,5,6,7,8,9]

def is_sub_prime(p,d,pos):
    new = replace(p,d,pos)
    return 1 if (len(str(new)) == len(str(p))
                 and is_prime(new)) else 0

def replace(p,d,pos):
    """Replace the digits at POS in p with d. Pos is a binary string with 1's where we will replace digits. Pos and p have the same length."""
    # if last digit will be replaced, then return 0 right away.
    l = len(str(p))
    temp = ""
    for i in range(l):
        if ((pos >>i)&1):
            temp = temp + str(d)
        else:
            temp = temp + str(p)[i]
    return int(temp)

def find_solution(p):
    l = len(str(p))
    for pos in range(1,2**(l-1)):
        total = sum(is_sub_prime(p,d,pos) for d in digits)
        if total >= 8:
            for d in digits:
                num = replace(p,d,pos)
                if (len(str(num)) == len(str(p)) and
                    is_prime(num)):
                    print(num)
                    sys.exit()

for p in candidates:
    find_solution(p)
