# Problem 87

#real	0m2.592s
#user	0m2.489s
#sys	0m0.071s
from utils import sieve

target = 50000000

quads = sieve(int(target ** (1/4)))
triples = sieve(int(target ** (1/3)))
doubles = sieve(int(target ** (1/2)))

vals = set()
for q in quads:
    for t in triples:
        for d in doubles:
            s = d**2 + t**3 + q**4
            if s < target:
                vals.add(s)

print(len(vals))
