#Problem 58
from utils import is_prime

# all the numbers on the corners of a square are as follows:
# side 1: 1
# n: previous max + i*(n-1) for i in range (1,4]

corners = [1]

iter_start = 1
max_width = 100000
prime_ratio = 1
cur_primes = 0
cur_total = 1
for i in range(2,max_width,2):
    for c in range(1,5):
        if is_prime(iter_start+i*c): cur_primes += 1
    cur_total += 4
    iter_start = iter_start + i*c
    prime_ratio = cur_primes/cur_total
    if (prime_ratio < 0.10):
        print(i+1)
        break

print(prime_ratio)
