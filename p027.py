# Problem 27
from utils import is_prime

def num_satisfying_primes(a,b):
    n = 0
    while (is_prime(n**2 + a*n + b)):
        n += 1
    return n

(max_a, max_b,max_n) = (-1000,-1000,0)

for a in range(-1000,1000):
    for b in range(-1000,1000):
        n = num_satisfying_primes(a,b)
        if (n > max_n):
            (max_a,max_b,max_n) = (a,b,n)

print (max_a,max_b,max_n)
print (max_a * max_b)
