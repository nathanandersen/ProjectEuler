# Problem 62
from itertools import permutations
import sys

# So, permutations is a 2^n level bit.
# There's a clever piece to look for here.

exit()



# Hideously slow.
def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x

def permutation_cube_count(x):
    digits = [digit for digit in str(x)]
    perms = permutations(digits)
    nums = {''.join(map(str,tup)) for tup in perms}
    return sum(is_perfect_cube(int(n)) for n in nums if len(str(int(n))) == len(digits))


for n in range(500,1000):
    pc = permutation_cube_count(n**3)
    print(n,pc)
    if pc == 5:
        print(n,n**3,pc)
        sys.exit()
