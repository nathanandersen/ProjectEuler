# Problem 46

# real 0m0.223s
# user 0m0.198s
# sys  0m0.013s

from utils import is_prime
import math

def solve():
    for i in range(35,10000,2):
        if is_prime(i):
            continue
        else:
            found_one = 0
            for x in range(1,int(math.sqrt(i)+1)):
                if is_prime(i-2*(x**2)):
                    found_one = 1
            if not found_one:
                return i


print(solve())
