# Problem 9
# a^2 + b^2 = c^2
# a + b + c = 1000
# Find abc

def solve():
    for a in range(1,1000):
        for b in range(1,1000):
            c = 1000 - a - b
            if not ((a**2) + (b**2) - (c**2)):
                return a*b*c
print(solve())
