# Problem 14

# This is really slow.
# real 0m43.262s
# user 0m42.627s
# sys  0m0.281s

# n -> n/2 (even)
# n -> 3n + 1 (odd)
from utils import collatz_steps

def max_collatz():
    (max,n) = (0,0)
    for i in range(1,1000000):
        steps = collatz_steps(i)
        if (steps > max):
            max = steps
            n = i
    return n
print(max_collatz())
