# Problem 387

# We want to build these right-truncatable... etc
# from the bottom up

from utils import is_prime
from utils import digit_sum
from queue import Queue

total = 0
q = Queue()
q.put(2)
q.put(3)
q.put(5)
q.put(7)
#nums = [2,3,5,7]
#target = 10 ** 14
#rTrunHarshads = set(nums)

def isStrongRightTruncatableHarshadPrime(n):
    if not is_prime(n):
        return False
    else:
        s = str(n)
        t = int(s[:len(s)-1])
        return isStrongHarshad(t)

def isRightTruncatableHarshad(n):
    if n < 10: return True
    s = str(n)
    t = int(s[:len(s)-1])
    return isHarshad(n) and t in prevTruncNums

def isStrongHarshad(n):
    d = digit_sum(n)
    return isHarshad(n) and is_prime(n//d)

def isHarshad(n):
    d = digit_sum(n)
    return ((n % d) == 0)

#twoPrevTruncNums = set()
prevTruncNums = set([n for n in range(10)])
curTruncNums = set()
nextNum = q.get()
#nextNum = nums.pop(0)
numLength = 1
while numLength < 14:
    for n in range(nextNum*10, nextNum*10 + 10):
#        if is_prime(n):
        if isStrongRightTruncatableHarshadPrime(n):
            print(n)
            total += n
        elif isRightTruncatableHarshad(n):# and isStrongHarshad(n):
            # Find a way to only save the previous layer
            curTruncNums.add(n)
            q.put(n)
#            nums.append(n)
    nextNum = q.get()
#    nextNum = nums.pop(0)
    if len(str(nextNum)) > numLength:
#        twoPrevTruncNums = prevTruncNums
        prevTruncNums = curTruncNums
        curTruncNums = set()
        numLength += 1
        print(numLength)

print(total)
