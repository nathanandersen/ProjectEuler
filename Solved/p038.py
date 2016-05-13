# Problem 38

# real 0m0.108s
# user 0m0.087s
# sys  0m0.012s

from utils import is_pandigital

def pandigital_multiple(n):
    num = ''
    a = 1
    while len(num) < 9:
        num += str(n*a)
        a += 1
    return num if is_pandigital(num) else 0

print(max(pandigital_multiple(n) for n in range(1,10000) if pandigital_multiple(n)))
