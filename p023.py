# Problem 23
from utils import factor_sum

abundants_set = set(list(x for x in range(1,28123) if factor_sum(x)>x))
def is_abundant(n):
    return factor_sum(n) > n

def is_abundant_sum(n):
    for i in abundants_set:
        if i > n:
            return False
        if (n-i) in abundants_set:
            return True
    return False

print(sum(list(x for x in range(1,28123) if not is_abundant_sum(x))))
