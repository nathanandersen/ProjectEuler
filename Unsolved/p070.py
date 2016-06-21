# Problem 70

from utils import phi
import sys

# Hideously, way too slow.
# We need to find a more effective way of doing this.
def phi_ratio_if_is_perm(n):
    val = phi(n)
    l = list(str(val))
    _l = list(str(n))
    if set(l) == set(_l):
        if sorted(l) == sorted(_l):
            return n/val
    return 2 # if no good

min_index = 0
min_val = sys.maxsize
for n in range(3,10**7,2):
    v = phi_ratio_if_is_perm(n)
    if v < min_val:
        print(n,v)
        (min_index,min_val) = (n,v)

print(min_index,min_val)
