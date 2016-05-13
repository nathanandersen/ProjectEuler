#Problem 60

from utils import is_prime
from utils import sieve
from itertools import combinations
import sys

primes = sieve(10000)
primes.remove(2)
primes.remove(5)
def is_concat_prime_set(primes):
    for p1 in primes:
        for p2 in primes:
            if p2 is not p1:
                if not concat_prime(p1,p2):
                    return 0
    return 1

def concat_prime(p1,p2):
    return is_prime(int(str(p1)+str(p2)))

def is_cc_prime_pair(pair):
    return (concat_prime(pair[0],pair[1]) and concat_prime(pair[1],pair[0]))

def is_valid_addition(prime,primes):
    for p in primes:
        if not (concat_prime(prime,p) and concat_prime(p,prime)):
            return 0
    return 1

# Let's create a dictionary / hashmap of PRIMES to OTHER PRIMES
# for which the pair is valid
pair_list = {2:[0]}

#Populate this dict
#for prime in primes:
#    print(prime)
#    valid_cc_primes = [p for p in primes if p != prime and is_cc_prime_pair(#(prime,p))]
#    pair_list[prime] = valid_cc_primes

# iterate over it and look for valid combos?
#for prime in primes:
#   count = len(pair_list[prime])
#    if (count > 4):
#        print(count,prime)






#pairs_of_primes =  {pair for pair in combinations(primes,2) if is_cc_prime_pair(pair)}
#print(pairs_of_primes)


#fives = combinations(primes,5)
#for five in fives:
#    if is_concat_prime_set(five):
#        print(five)
#        sys.exit()
quads = combinations(primes,4)
quad_sets = []
# SETS UNDER 5000
#(3, 7, 109, 673)
#(3, 7, 541, 4159)
#(3, 11, 2069, 2297)
#(3, 17, 449, 2069)
#(3, 17, 2069, 2297)
#(3, 37, 67, 2377)
#(3, 37, 2377, 4159)
#(3, 467, 617, 4253)
#(7, 19, 97, 3727)
#(7, 19, 97, 4507)
#(7, 19, 1249, 3727)
#(7, 61, 1693, 3181)
#(7, 433, 1471, 3613)
#(7, 829, 2671, 3361)
#(7, 1237, 1549, 3019)
#(7, 2089, 2953, 3181)
#(7, 2089, 3181, 4219)
#(11, 23, 743, 1871)
#(11, 239, 1049, 1847)
#(11, 239, 1091, 1847)
#(17, 2741, 3917, 4649)
#(23, 47, 1481, 4211)
#(23, 311, 677, 827)
#(23, 677, 827, 1871)
#(31, 1123, 2029, 2281)
#(37, 991, 2269, 3613)
#(37, 1549, 2707, 3463)
# continue checking starting at 37


for quad in quads:
    if is_concat_prime_set(quad):
        print(quad)
        quad_sets.append(quad)
for prime in primes:
    for qs in quad_sets:
        if is_valid_addition(prime,qs):
            print(prime,qs)
