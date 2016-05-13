# Problem 63
import math
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
