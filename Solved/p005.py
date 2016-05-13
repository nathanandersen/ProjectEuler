# Problem 5

# real 0m0.103s
# user 0m0.057s
# sys  0m0.017s

import math
from utils import lcm
cur_lcm = 1

for i in range(20,1,-1):
    cur_lcm = lcm(cur_lcm,i)
print(cur_lcm)
