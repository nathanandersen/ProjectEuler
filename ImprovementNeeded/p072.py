# Problem 72
from utils import gcd
from utils import factor_count
from utils import phi

#real	0m46.211s
#user	0m44.369s
#sys	0m0.393s

# notes:
# primes introduce p-1 new fractions

# composites introduce phi more, where phi = the number
# of relatively prime #s less than n


print(sum(phi(n) for n in range(2,1000001)))
#total = 0
#for n in range(2,1000001):
#    total += phi(n)
#print(total)
