# Problem 12.

# real 0m1.868s
# user 0m1.667s
# sys  0m0.089s

from utils import factor_count
from utils import triangular_num

n = 10000
while(factor_count(triangular_num(n)) < 500):
    n += 1
print(triangular_num(n))
