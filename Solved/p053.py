#Problem 53

# real 0m0.072s
# user 0m0.052s
# sys  0m0.012s

from utils import choose

num = 0

for n in range(1,101):
    for r in range(4,n-2):
       num += 1 if choose(n,r) > 1000000 else 0
print(num)
