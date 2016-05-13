# Problem 49
from utils import sieve
from itertools import permutations
from utils import is_prime

primes = {p for p in sieve(10000) if len(str(p)) == 4}

def solve():
    for p in primes:
        # something something permutations
        digits = [digit for digit in str(p)]
        nums = []
        for perm in permutations(digits):
            nums.append(''.join(str(d) for d in perm))
            # Ok, so now I have all the 4 bit rotated numbers.
            solution_nums = {int(num) for num in nums if int(num) in primes}
            if(len(solution_nums) <4): continue
            for n in solution_nums:
                if (n-p == 3330 and n+3330 in solution_nums):
                    return(p,n,n+3330)

print(solve())
