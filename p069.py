# Problem 69
from utils import gcd
from utils import is_prime
from utils import factors
# This is a pretty slow implementation. Let's see if we can
# speed it up

# if gcd(i,n) == 1, then all factors of it will also have gcd
# so maybe i should iterate down from the top?

#def phi(n):
#    amt = 0
#    for k in range(1,n):
#        if gcd(k,n) == 1:
#            amt += 1
#    return amt

def phi(n):
    unique = []
    totient = n
    for p in factors(n):
        if p not in unique:
            unique.append(p)
            totient -= totient//p # integer division
    return totient
#    return output

max_val = 0
for n in range(3,1000000,6):
    print(n)
    max_val = max(max_val, n/phi(n))
print(max_val)
