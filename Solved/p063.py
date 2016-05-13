# Problem 63
import math

# real 0m0.046s
# user 0m0.026s
# sys 0m0.010s

# 10^n-1 <= x^n <= 10^n
# upper bound clearly 10
# 10^n-1 <= x^n
# n-1 <= log(x) * n
# (n-1)/n <= log(x)
# 10 ^ (n-1)/n <= x <=

#upper_bd = 10
lower_bd = 0
count = 0
n = 1
while (lower_bd < 10):
    lower_bd = (int)(math.ceil(10 ** ((n-1)/n)))
    count += (10-lower_bd)
    n += 1

print(count)
