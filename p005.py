# Problem 5
# Smallest number divisible by all the numbers 1-20
import math
from utils import lcm
cur_lcm = 1

for i in range(20,1,-1):
    cur_lcm = lcm(cur_lcm,i)
print(cur_lcm)
