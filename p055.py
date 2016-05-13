# Problem 55
# Lychrel numbers
from utils import is_palindrome

def is_lychrel(n):
    num = n
    for i in range(50):
        num += int(str(num)[::-1])
        if is_palindrome(num): return 0
    return 1

print(sum(1 for n in range(10,10000) if is_lychrel(n)))
#print(is_lychrel(47))
#print(is_lychrel(349))
