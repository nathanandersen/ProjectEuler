# Problem 80
from decimal import *
from utils import digit_sum
from utils import is_square_num

getcontext().prec = 102 #enough past the decimal

def sqrt_digit_sum(n):
    target = Decimal(n).sqrt()
    return digit_sum(str(target)[2:101:]) + int(target)

print(sqrt_digit_sum(2))
count = 0
for i in range(1,101):
    if not is_square_num(i):
        count += sqrt_digit_sum(i)

print(count)
