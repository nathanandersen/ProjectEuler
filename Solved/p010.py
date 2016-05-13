# Problem 10

# real 0m0.389s
# user 0m0.318s
# sys  0m0.062s

from utils import sieve

print(sum(p for p in sieve(2000000)))
