# Problem 33

# real 0m0.090s
# user 0m0.046s
# sys  0m0.012s

from fractions import gcd
solutions = []

def is_cancellable(a,b):
    a = str(a)
    b = str(b)
    if a[:1] == b[:1] and int(b[1:2]) and int(a[:1]):
        if int(a[1:2])/int(b[1:2]) == int(a)/int(b):
            return True
    if a[:1] == b[1:2] and int(b[:1]) and int(a[:1]):
        if int(a[1:2])/int(b[:1]) == int(a)/int(b):
            return True
    if a[1:2] == b[:1] and int(b[1:2]) and int(a[1:2]):
        if int(a[:1])/int(b[1:2]) == int(a)/int(b):
            return True
    if a[1:2] == b[1:2] and int(b[:1]) and int(a[1:2]):
        if int(a[:1])/int(b[:1]) == int(a)/int(b):
            return True
    return False

def reduce_fraction(a,b):
    return (int(a/gcd(a,b)),int(b/gcd(a,b)))

for b in range(10,100):
    for a in range(10,b):
        solutions.append([a,b]) if is_cancellable(a,b) else 0

numerator = 1
denominator = 1
for x in solutions:
    numerator *= x[0]
    denominator *= x[1]
(numerator,denominator) = (reduce_fraction(numerator,denominator))
print(denominator)
