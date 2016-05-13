#Problem 56
from utils import digit_sum

max_digit_sum = 0
for a in range(100):
    for b in range(100):
        max_digit_sum = max(max_digit_sum,digit_sum(a**b))

print(max_digit_sum)
