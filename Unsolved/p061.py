# Problem 61

from utils import is_triangular_num
from utils import is_square_num
from utils import is_pent_num
from utils import is_hex_num
from utils import is_hept_num
from utils import is_oct_num

tri_nums = set()
sq_nums = set()
pent_nums = set()
hex_nums = set()
hept_nums = set()
oct_nums = set()

# can we build a suffix tree for this?



# construct sets of all nums
for n in range(1000,10000):
    if is_triangular_num(n): tri_nums.add(n)
    if is_square_num(n): sq_nums.add(n)
    if is_pent_num(n): pent_nums.add(n)
    if is_hex_num(n): hex_nums.add(n)
    if is_hept_num(n): hept_nums.add(n)
    if is_oct_num(n): oct_nums.add(n)

def is_of_a_type(n):
    return (n in tri_nums or
            n in sq_nums or
            n in pent_nums or
            n in hex_nums or
            n in hept_nums or
            n in oct_nums)

for n in range(1000,10000):
    pass

