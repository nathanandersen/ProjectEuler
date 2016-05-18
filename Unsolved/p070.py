# Problem 70

from utils import phi
import sys
from itertools import permutations

def phi_ratio_if_is_perm(n):
    val = phi(n)
    perms = set(permutations(str(val)))
    if n in perms:
        return n/val
    else: return 0

min_index = 0
min_val = sys.maxsize
for n in range(2,10000000):
    v = phi_ratio_if_is_perm(n)
    if v is not 0 and v < min_val:
        print(v)
        (min_index,min_val) = (n,v)

print(max_index,max_val)
