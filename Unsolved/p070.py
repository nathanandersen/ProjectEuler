# Problem 70

from utils import phi
import sys

# Hideously, way too slow.
# We need to find a more effective way of doing this.
def phi_ratio_if_is_perm(n):
    val = phi(n)
    l = sorted(list(str(val)))
    if sorted(list(str(n))) == l:
        return n/val
    else: return sys.maxsize # not mathemetically possible

min_index = 0
min_val = sys.maxsize
for n in range(2,10000000):
    v = phi_ratio_if_is_perm(n)
    if v < min_val:
        print(n,v)
        (min_index,min_val) = (n,v)

print(min_index,min_val)
