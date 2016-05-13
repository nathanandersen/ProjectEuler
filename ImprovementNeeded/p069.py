# Problem 69
from utils import phi

# real 0m46.118s
# user 0m45.483s
# sys  0m0.283s

max_val = 0
max_index = 0
for n in range(1,1000000):
    ratio = n/phi(n)
    if ratio > max_val:
        max_val = ratio
        max_index = n
    
print(max_index,max_val)
