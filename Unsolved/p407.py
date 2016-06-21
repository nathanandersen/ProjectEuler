# Problem 407

# Hmm these seems familiar, from discrete math.
# There's a cool property here, but what?

def findM(n):
    for a in reversed(range(n)):
        if (a**2) % n == a:
            return a
    return -1

total = 0
for n in range(1,10**7 + 1):
    total += findM(n)
    print(n)

print(total)
