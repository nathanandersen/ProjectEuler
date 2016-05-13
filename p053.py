#Problem 53
from utils import choose

num = 0

for n in range(1,101):
    for r in range(4,n-2):
       num += 1 if choose(n,r) > 1000000 else 0
print(num)
