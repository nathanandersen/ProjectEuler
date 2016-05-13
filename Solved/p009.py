# Problem 9

# real 0m0.298s
# user 0m0.277s
# sys  0m0.011s

def solve():
    for a in range(1,1000):
        for b in range(1,1000):
            c = 1000 - a - b
            if not ((a**2) + (b**2) - (c**2)):
                return a*b*c
print(solve())
