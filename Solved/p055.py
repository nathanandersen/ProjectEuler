# Problem 55

# real 0m0.141s
# user 0m0.118s
# sys  0m0.013s

from utils import is_palindrome

def is_lychrel(n):
    num = n
    for i in range(50):
        num += int(str(num)[::-1])
        if is_palindrome(num): return False
    return True

print(sum(1 for n in range(10,10000) if is_lychrel(n)))
