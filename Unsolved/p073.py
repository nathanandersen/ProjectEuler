# Problem 73

#from utils import phi
from utils import gcd
#import queue
import math

#all_fracs = queue.PriorityQueue()

def add_to_fracs(n):
    count = 0
#    j = 0
#    for k in range(n//3,n):
#        if k/n > 1/3:
#            j = k
#            break
    for i in range(n//3,(n//2)+n%2):
        if gcd(i,n) == 1: count += 1
    return count

total = 0
for n in range(8):
    print(n)
    total += add_to_fracs(n)

print(total)
