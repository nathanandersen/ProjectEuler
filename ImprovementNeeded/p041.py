# Problem 41
from utils import is_prime
from utils import is_pandigital

print(max(i for i in range(7654321) if is_pandigital(i) and is_prime(i)))

# Some observations about pandigital numbers:
# if they have 9 digits, then they are divisible by 3
# if they have 8 digits, then they are divisble by 3.
# biggest 7 digit pan number = 7654321
