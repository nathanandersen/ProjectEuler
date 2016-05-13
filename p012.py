# Problem 12.
# Find the first triangular number to have over 500 factors.
# A triangular number is defined as sum(n) for i in range(1,n),inclusive
import math
from utils import factor_count
from utils import triangular_num

n = 1
while(factor_count(triangular_num(n)) < 500):
    n += 1
print(triangular_num(n))
