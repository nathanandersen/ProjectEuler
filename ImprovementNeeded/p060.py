#Problem 60

# A set-implementing DP.

# real	0m22.076s
# user	0m21.806s
# sys	0m0.120s


from utils import is_prime
from utils import sieve
from itertools import product


primes = sieve(10000)
primes.remove(2)
primes.remove(5)

pairs = set()
triples = set()
quads = set()
fives = set()

def is_concat_pair(a,b):
    return (a < b and
            is_prime(int(str(a)+str(b))) and
            is_prime(int(str(b)+str(a))))

def find_pairs():
    for (a,b)in product(primes,repeat=2):
        if is_concat_pair(a,b):
            pairs.add((a,b))

def find_triples():
    for (a,(b,c)) in product(primes,pairs):
        if (a,b) in pairs and (a,c) in pairs:
            triples.add((a,b,c))

def find_quads():
    for (a,(b,c,d)) in product(primes,triples):
        if ((a,b,c) in triples and
            (a,b,d) in triples and
            (a,c,d) in triples):
            quads.add((a,b,c,d))

def find_fives():
    for (a,(b,c,d,e)) in product(primes,quads):
        if ((a,b,c,d) in quads and
            (a,b,c,e) in quads and
            (a,b,d,e) in quads and
            (a,c,d,e) in quads):
            print(a+b+c+d+e)
#            print(a,b,c,d,e)
            fives.add((a,b,c,d,e))


def solve():
    find_pairs()
#    print("pairs finished")
    find_triples()
#    print("triples finished")
    find_quads()
#    print("quads finished")
    find_fives()

solve()
