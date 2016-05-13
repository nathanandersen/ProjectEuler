# Problem 61
from utils import is_triangular_num
from utils import is_square_num
from utils import is_pent_num
from utils import is_hex_num
from utils import is_hept_num
from utils import is_oct_num
from itertools import product

four_digit_nums = range(1000,10000)
# Create data structures that have numbers, and associations with
# the first 2 digits (prefix) and last 2 digits (suffix)
tris = []
tri_prefixes = {0:0}
tri_suffixes = {0:0}
squares = []
sq_prefixes = {0:0}
sq_suffixes = {0:0}
pents = []
pent_prefixes = {0:0}
pent_suffixes = {0:0}
hexes = []
hex_prefixes = {0:0}
hex_suffixes = {0:0}
hepts = []
hept_prefixes = {0:0}
hept_suffixes = {0:0}
octs = []
oct_prefixes = {0:0}
oct_suffixes = {0:0}
for f in four_digit_nums:
    if is_triangular_num(f):
        tris.append(f)
        tri_prefixes[int(str(f)[0:2])] = f
        tri_suffixes[int(str(f)[2:4])] = f
    if is_square_num(f):
        squares.append(f)
        sq_prefixes[int(str(f)[0:2])] = f
        sq_suffixes[int(str(f)[2:4])] = f
    if is_pent_num(f):
        pents.append(f)
        pent_prefixes[int(str(f)[0:2])] = f
        pent_suffixes[int(str(f)[2:4])] = f
    if is_hex_num(f):
        hexes.append(f)
        hex_prefixes[int(str(f)[0:2])] = f
        hex_suffixes[int(str(f)[2:4])] = f
    if is_hept_num(f):
        hepts.append(f)
        hept_prefixes[int(str(f)[0:2])] = f
        hept_suffixes[int(str(f)[2:4])] = f
    if is_oct_num(f):
        octs.append(f)
        oct_prefixes[int(str(f)[0:2])] = f
        oct_suffixes[int(str(f)[2:4])] = f


# Now i have all the four digit sets.

for t in tris:
    h = hept_suffixes.get(int(str(t)[0:2]),0)
    if h: print(h,t)
    h = hept_prefixes.get(int(str(t)[2:4]),0)
    if h: print(t,h)
#for t in tris:
    # try and find a matching number of each
    # type with the next?
