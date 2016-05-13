# Problem 21

# real 0m0.267s
# user 0m0.243s
# sys  0m0.014s

# Amicable numbers
# d(n) = the aliquot sum of n (factor sum)
# if d(a) = b, d(b) = a, then (a,b) is an amicable pair

# For example
# d(220) = 284
# d(284) = 220

# Find sum of all amicable numbers under 10000
#import math
from utils import factor_sum

def is_amicable(x):
    return x == factor_sum(factor_sum(x)) and x != factor_sum(x)

print(sum(n if is_amicable(n) else 0 for n in range(1,10000)))

