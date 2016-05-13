# Problem 23

# real 0m1.226s
# user 0m1.200s
# sys  0m0.014s

from utils import factor_sum

abundants_set = set(x for x in range(1,28123) if factor_sum(x)>x)
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
