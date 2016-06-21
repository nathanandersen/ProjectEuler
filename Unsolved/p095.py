# Problem 95
from utils import factors

def nextAmicableNum(n):
    return sum(factors(n))

accountedFor = set()

#s = set()
#for n in range(1000000):
#    s.add(n)

maxChain = set()
curChain = set()
n = 1
#for n in range(1,1000000):
while n < 1000000:
    if n not in accountedFor:
        num = n
        print(num)
        while True:
            if num in curChain:
                break
            elif num in accountedFor or num > 1000000:
                curChain = set()
                break
            else:
                accountedFor.add(num)
                curChain.add(num)
                num = nextAmicableNum(num)
        if len(curChain) > len(maxChain):
            maxChain = curChain.copy()
            curChain = set()
#    print(n)
    n += 1

print("finished")
print(min(maxChain))
