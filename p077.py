# Problem 77
primes = sieve(1000)

def take_steps(n,largest):
    total = 1
    if n < 0:
        return 0
    if n == 2:
        return 1
    for i in primes:
        # complete me according to p076
