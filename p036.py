# Problem 36

from utils import is_palindrome
from utils import dec_to_bin

print(sum(n for n in range(1000000) if is_palindrome(n) and is_palindrome(dec_to_bin(n))))
