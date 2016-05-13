#Problem 4
# Largest palindromic project
#Find the largest palindrome made from the project of two 3-digit numbers
from utils import is_palindrome

def find_palindromes(a,b):
    options = []
    for i in reversed(range(a,b)):
        for j in reversed(range(a,b)):
            options.append(i*j) if is_palindrome(i*j) else 0
    return max(options)

print (find_palindromes(100,1000))
