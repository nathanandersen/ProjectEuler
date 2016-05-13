#Problem 34
from math import factorial

def is_digit_factorial(n):
    return n > 2 and n == sum(factorial(int(digit)) for digit in str(n))
print(sum(x for x in range(2540160) if is_digit_factorial(x)))
