# A package to have useful methods
"""Useful methods for Project Euler"""
import math
import fractions

def is_square_num(s):
    """Returns whether s is a square or not."""
    n = math.sqrt(s)
    return int(n) if n.is_integer() else 0
def hept_num(n):
    """Returns the nth heptagonal number."""
    return int(n*(5*n-3)/2)

def is_hept_num(h):
    """Returns n for which h is the nth heptagonal number."""
    n = (math.sqrt(40*h + 9) + 3)/10
    return int(n) if n.is_integer() else 0

def oct_num(n):
    """Returns the nth octagonal number."""
    return n*(3*n-2)

def is_oct_num(o):
    """Returns n for which o is the nth octagonal number."""
    n = (math.sqrt(3*o + 1)+1)/3
    return int(n) if n.is_integer() else 0

def lcm(a,b):
    """Return the least common multiple of a and b."""
    return int(a*b/gcd(a,b))

def gcd(a,b):
    """Return the greatest common divisor of a and b."""
    return int(fractions.gcd(a,b))

def choose(n,r):
    """Return n choose r."""
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

def hex_num(n):
    """Returns the nth hexagonal number."""
    return n*(2*n-1) if n > 0 else 0

def is_hex_num(h):
    """Returns n, for which h is the nth hexagonal number."""
    if h <= 0:
        return 0
    n = (math.sqrt(8*h+1)+1)/4
    return int(n) if n.is_integer() else 0

def pent_num(n):
    """Returns the nth pentagonal number."""
    return int(n*(3*n-1)/2) if n > 0 else 0

def is_pent_num(p):
    """Returns n, for which p is the nth pentagonal number."""
    if p <= 0:
        return 0
    n = (math.sqrt(24*p+1)+1)/6
    return int(n) if n.is_integer() else 0

def clean_list_file(fn):
    """Returns a clean list, given a comma-delimited file."""
    with open(fn,"r") as f:
        for text in f:
            text = eval("[" + text + "]")
    return text

def is_right_triangle(a,b,c):
    """Returns whether the tuple(a,b,c) is a right triangle"""
    return a**2 + b**2 == c**2

def is_pandigital(x):
    """Returns whether x is a pandigital number."""
    if len(str(x)) == 10:
        return triangular_num(len(str(x))-1) == digit_sum(x) and len(str(x)) == len(set([digit for digit in str(x) if int(digit)]))
    elif len(str(x)) < 10:
        return triangular_num(len(str(x))) == digit_sum(x) and len(str(x)) == len(set([digit for digit in str(x) if int(digit)]))
    else: return 0


def dec_to_bin(n):
    """Print the binary representation of a decimal number."""
    return str(bin(n))[2:]

def next_fibonacci(p,c):
    """Takes the previous two numbers and returns their sum (ie the next Fibonacci number)."""
    return p+c

def next_fibonacci_set(p1,p2,c,n):
    """Takes the previous two numbers (and the current one), and returns the set of the next three. Useful when you always want to maintain 3 Fibonacci numbers, you can just set that tuple equal to this one. N is the index of the current Fibonacci number."""
    return (p2,c,p2+c,n+1)

def fibonacci(n):
    """Returns the nth fibonacci number."""
    return 1 if n==0 else 1 if n==1 else fibonacci(n-1) + fibonacci(n-2)

def word_value(w):
    """Returns the sum total of the letter values in the word."""
    return sum(letter_value(letter) for letter in w)

def letter_value(c):
    """Returns the letter value. a=1, b=2,.."""
    return 1+ord(c.upper())-ord('A')

def digit_sum(n):
    """Returns the sum of all digits in the string/number"""
    return sum(int(digit) for digit in str(n))

def collatz_steps(n):
    i = 1
    while (n-1):
        n = 3*n+1 if n%2 else n/2
        i += 1
    return i

def is_triangular_num(n):
    """Returns x for which n is the x-th triangular number (or 0)."""
    x = (math.sqrt(8*n+1)-1)/2
    return x.is_integer()

def triangular_num(n):
    """Returns the n-th triangular number."""
    return int(n*(n+1)/2) if n > 0 else 0

def factor_count(n):
    """Returns the factor count of the input"""
    return(len(factors(n)))

def is_palindrome(a):
    """Returns whether the input is a palindrome for any input."""
    return str(a) == str(a)[::-1]

def prime_factors(n):
    return set([f for f in factors(n) if is_prime(f)])

def factors(n):
    """The set of all the factors of n"""
    factors = [1]
    for i in range(2,int(math.sqrt(n)+1)):
        if not n%i:
            factors.append(i)
            factors.append(int(n/i))
    if int(math.sqrt(n)) ** 2 == n:
        factors.remove(int(math.sqrt(n)))
    return set(factors)

def factor_sum(n):
    """The sum of all the factors of n."""
    return(sum(factors(n)))


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(math.sqrt(n))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    s = [ele_s for ele_s in s if ele_s and ele_s is not None]
    return s
#    return filter(None, s)

from bisect import bisect_left
# sqrt(1000000000) = 31622
__primes = sieve(31622)
def is_prime(n):
    """Returns whether a number is prime or not"""
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True

#def is_prime(n):
#    """Returns whether n is prime or not."""
#    return n > 1 and n%2 and all(n%i for i in range(3,int(math.sqrt(n))+1,2))
