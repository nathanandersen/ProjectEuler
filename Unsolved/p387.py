# Problem 387

# We want to build these right-truncatable... etc
# from the bottom up
from utils import is_prime
from utils import digit_sum
from queue import Queue

total = 0
q = Queue()
for n in range(1,10):
    # All single digit numbers are starters
    q.put(n)

def isStrongRightTruncatableHarshadPrime(n):
    if not is_prime(n):
        return False
    else:
        s = str(n)
        t = int(s[:len(s)-1])
        return isStrongHarshad(t)

def isStrongHarshad(n):
    if isHarshad(n):
        r = n/digit_sum(n)
        if (r).is_integer():
            return is_prime(r)
    return False

def isHarshad(n):
    d = digit_sum(n)
    return ((n % d) == 0)

nextNum = q.get()
while len(str(nextNum)) < 14:
    if isStrongHarshad(nextNum):
        for n in range(10):
            if is_prime(nextNum*10 + n):
                print(nextNum*10 + n)
                total +=nextNum*10 + n
    for n in range(10):
        if isHarshad(nextNum*10 + n): # Simple test because we are
        # only building from right truncatable harshads
            q.put(nextNum*10 + n)
    nextNum = q.get()

print(total)
