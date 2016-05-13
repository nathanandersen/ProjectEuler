#Problem 45
from utils import hex_num
from utils import is_hex_num
from utils import pent_num
from utils import is_pent_num
from utils import triangular_num


tri_nums = [triangular_num(i) for i in range(100000)]

max_num = 40755
for t in tri_nums:
    if (is_hex_num(t) and
        is_pent_num(t)):
        max_num = t

print(max_num)
