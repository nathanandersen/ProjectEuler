# Problem 145


# Brute forcing..
m = 10 ** 9

def isReversible(n):
    r = int(str(n)[::-1])
    r = set(str(n + r))
    for n in '24680':
        if n in r: return False
    return True

total = 0
for n in range(1,m):
    if isReversible(n):
        total += 1
        print(n)
