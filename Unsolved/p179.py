# Problem 179
from utils import factor_count

# How can I make this into a DP?
# I want to use GCD

def inclusiveFactorCount(n):
    return 1 + factor_count(n)

total = 0
topLimit = 10**7
prevCt = inclusiveFactorCount(2)
for n in range(3,topLimit+1):
    ifc = inclusiveFactorCount(n)
    if ifc == prevCt:
        total += 1
    prevCt = ifc
    print(n)

print(total)
