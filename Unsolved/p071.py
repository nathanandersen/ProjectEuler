# Problem 71
from utils import factors
from utils import gcd
from fractions import Fraction


def factorial(n):
    fact = 1
    while n:
        fact *= n
        n -= 1
    return fact

def find_max_fraction(n):
    # less than 1/7
    fs = factors(n)
    max_n = 0
    for k in range(n):
        if (k/n) >= (1/7): return max_n
        if gcd(k,n) == 1:
                max_n = k


if __name__ == "__main__":
#    print(factorial(1000001))
    exit()
    max_n = 1
    max_d = 1000
    for d in range(2,10000):
        print(d)
        n = find_max_fraction(d)
        if (n/d) > (max_n/max_d):
            max_n = n
            max_d = d

    print(max_n,max_d)
