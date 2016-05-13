# Problem 25
# The first Fibonacci term to contain 1000 digits
from utils import next_fibonacci_set
p1 = 1
p2 = 1
cur = 2
n = 3
while (len(str(cur)) < 1000):
    (p1,p2,cur,n) = next_fibonacci_set(p1,p2,cur,n)
print(n)
