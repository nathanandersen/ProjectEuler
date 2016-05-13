#Problem 32
#
from itertools import permutations

digits = [1,2,3,4,5,6,7,8,9]
seq = []

for p in permutations(digits):
    seq.append(''.join(str(e) for e in p))

global pans
pans = []
def find_pans(seq):
    for s in seq:
        for a in range(1,4): # 1 2 3
            for b in range(1,6-a): # 1 2 3 .. 5?
                if int(s[0:a]) * int(s[a:a+b]) == int(s[a+b:len(s)]):
                    pans.append(int(s[a+b:]))

find_pans(seq)
#find_pans(["391867254"])
pans = set(pans)
print(pans)

print(sum(pans))
