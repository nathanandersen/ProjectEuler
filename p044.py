# Problem 44
from utils import pent_num
from utils import is_pent_num

min_diff = 10000000
pents = [pent_num(i) for i in range(1,10000)]
for k in range(0,9999):
    for j in range(0,9999):
        if (k-j and
            is_pent_num(abs(pents[k]-pents[j])) and
            is_pent_num(pents[k]+pents[j]) and
            abs(pents[k]-pents[j]) < min_diff):
            min_diff = abs(pents[k]-pents[j])

print(min_diff)
