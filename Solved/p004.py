#Problem 4

# real 0m1.147s
# user 0m1.025s
# sys  0m0.057s

from utils import is_palindrome

def find_palindromes(a,b):
    options = []
    for i in reversed(range(a,b)):
        for j in reversed(range(a,b)):
            if is_palindrome(i*j):
                options.append(i*j)
    return max(options)

print (find_palindromes(100,1000))
